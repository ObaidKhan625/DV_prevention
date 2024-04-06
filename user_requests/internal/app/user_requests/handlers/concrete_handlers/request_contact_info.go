package concrete_handlers

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	sq "github.com/Masterminds/squirrel"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/pkg/postgres"
	"github.com/jackc/pgx/v5"
	"net/http"
)

type RequestContactInfo struct {
}

func (rci RequestContactInfo) HandleRequest(w http.ResponseWriter, r *http.Request) {
	rci.SetResponseOnWriter(w)

	userIdToBeContacted := r.URL.Query().Get("user_id")

	// todo: Get from auth service
	currentUserId := "1"

	if currentUserId == userIdToBeContacted {
		rci.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	conn, err := pgx.Connect(context.Background(), "postgres://postgres:@localhost/user_request")
	if err != nil {
		fmt.Printf("Unable to connect to database: %v\n", err)
		rci.SetUnsuccessfulResponseOnWriter(w)
		return
	}
	defer conn.Close(context.Background())

	contactRequestExists := rci.ExistsInDB(userIdToBeContacted, currentUserId, conn)
	if contactRequestExists {
		rci.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	err = rci.AddToDB(userIdToBeContacted, currentUserId, conn)
	fmt.Println("Insert error : ", err)

	// todo: Send data to channel
}

func (rci RequestContactInfo) ExistsInDB(recipientUserId string, actorUserId string, conn *pgx.Conn) bool {
	contactRequestExistsSQL :=
		sq.Select("1").
			From("contact_request").
			Where(sq.Eq{
				"requested_user_id":  recipientUserId,
				"requesting_user_id": actorUserId,
			}).
			PlaceholderFormat(sq.Dollar).
			Limit(1)

	sql, args, _ := contactRequestExistsSQL.ToSql()

	resultFlag := 0
	err := conn.QueryRow(context.Background(), sql, args...).Scan(&resultFlag)
	if err != nil && errors.Is(err, pgx.ErrNoRows) {
		return false
	}
	return true
}

func (rci RequestContactInfo) AddToDB(recipientUserId string, actorUserId string, conn *pgx.Conn) error {
	psql := sq.StatementBuilder.PlaceholderFormat(sq.Dollar)
	insertContactRequestSQL := psql.Insert("contact_request").
		Columns("requested_user_id", "requesting_user_id").
		Values(recipientUserId, actorUserId)
	return postgres.ExecQueryFromBuilder(insertContactRequestSQL, conn)
}

func (rci RequestContactInfo) GetFromDB() []handlers.UserRequest {
	return []handlers.UserRequest{}
}

func (rci RequestContactInfo) SetUnsuccessfulResponseOnWriter(w http.ResponseWriter) {
	responseData := map[string]any{
		"report_post": false,
	}
	jsonResponse, _ := json.Marshal(responseData)
	_, _ = w.Write(jsonResponse)
}

func (rci RequestContactInfo) SetResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
}

func NewRequestContactInfoHandler() *RequestContactInfo {
	return &RequestContactInfo{}
}
