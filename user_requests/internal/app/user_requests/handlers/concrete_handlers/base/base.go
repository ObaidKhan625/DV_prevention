package base

import (
	"context"
	"fmt"
	sq "github.com/Masterminds/squirrel"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/pkg/postgres"
	"github.com/jackc/pgx/v5"
	"net/http"
)

type BaseHandler struct {
	input Input
}

func (b BaseHandler) HandleRequest(w http.ResponseWriter, r *http.Request) {
	b.SetResponseOnWriter(w)

	recipientUserId := r.URL.Query().Get("user_id")

	// todo: Get from auth service
	currentUserId := "1"

	if currentUserId == recipientUserId {
		b.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	conn, err := pgx.Connect(context.Background(), "postgres://postgres:@localhost/user_request")
	if err != nil {
		fmt.Printf("Unable to connect to database: %v\n", err)
		b.SetUnsuccessfulResponseOnWriter(w)
		return
	}
	defer conn.Close(context.Background())

	reportExists := b.ExistsInDB(recipientUserId, currentUserId, conn)
	if reportExists {
		b.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	err = b.AddToDB(recipientUserId, currentUserId, conn)
	fmt.Println("Insert error : ", err)
}

func (b BaseHandler) ExistsInDB(recipientUserId string, actorUserId string, conn *pgx.Conn) bool {
	reportExistsSQL :=
		sq.Select("1").
			From(b.input.TableName).
			Where(sq.Eq{
				b.input.RecipientColumnName: recipientUserId,
				b.input.ActorColumnName:     actorUserId,
			}).
			PlaceholderFormat(sq.Dollar).
			Limit(1)

	return postgres.CheckIfRecordsExist(reportExistsSQL, conn)
}

func (b BaseHandler) AddToDB(recipientUserId string, actorUserId string, conn *pgx.Conn) error {
	psql := sq.StatementBuilder.PlaceholderFormat(sq.Dollar)
	insertBuilder := psql.Insert(b.input.TableName).
		Columns(b.input.RecipientColumnName, b.input.ActorColumnName).
		Values(recipientUserId, actorUserId)
	return postgres.ExecQueryFromBuilder(insertBuilder, conn)
}

func (b BaseHandler) GetFromDB() []handlers.UserRequest {
	return []handlers.UserRequest{}
}

func (b BaseHandler) SetUnsuccessfulResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusNoContent)
}

func (b BaseHandler) SetResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
}

func NewBaseHandler(input Input) *BaseHandler {
	return &BaseHandler{
		input: input,
	}
}
