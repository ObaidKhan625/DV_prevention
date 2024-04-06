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

type VerifyUser struct {
}

func (vu VerifyUser) HandleRequest(w http.ResponseWriter, r *http.Request) {
	vu.SetResponseOnWriter(w)

	userIdToBeVerified := r.URL.Query().Get("user_id")

	// todo: Get from auth service
	currentUserId := "1"

	if currentUserId == userIdToBeVerified {
		vu.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	conn, err := pgx.Connect(context.Background(), "postgres://postgres:@localhost/user_request")
	if err != nil {
		fmt.Printf("Unable to connect to database: %v\n", err)
		vu.SetUnsuccessfulResponseOnWriter(w)
		return
	}
	defer conn.Close(context.Background())

	verificationExists := vu.ExistsInDB(userIdToBeVerified, currentUserId, conn)
	if verificationExists {
		vu.SetUnsuccessfulResponseOnWriter(w)
		return
	}

	err = vu.AddToDB(userIdToBeVerified, currentUserId, conn)
	fmt.Println("Insert error : ", err)
}

func (vu VerifyUser) ExistsInDB(userIdToBeVerified string, verifyingUserId string, conn *pgx.Conn) bool {
	verificationExistsSQL :=
		sq.Select("1").
			From("verification").
			Where(sq.Eq{
				"verified_user_id":  userIdToBeVerified,
				"verifying_user_id": verifyingUserId,
			}).
			PlaceholderFormat(sq.Dollar).
			Limit(1)

	sql, args, _ := verificationExistsSQL.ToSql()

	resultFlag := 0
	err := conn.QueryRow(context.Background(), sql, args...).Scan(&resultFlag)
	if err != nil && errors.Is(err, pgx.ErrNoRows) {
		return false
	}
	return true
}

func (vu VerifyUser) AddToDB(verifiedUserId string, verifyingUserId string, conn *pgx.Conn) error {
	psql := sq.StatementBuilder.PlaceholderFormat(sq.Dollar)
	insertVerificationSQL := psql.Insert("verification").
		Columns("verified_user_id", "verifying_user_id").
		Values(verifiedUserId, verifyingUserId)
	return postgres.ExecQueryFromBuilder(insertVerificationSQL, conn)
}

func (vu VerifyUser) GetFromDB() []handlers.UserRequest {
	return []handlers.UserRequest{}
}

func (vu VerifyUser) SetUnsuccessfulResponseOnWriter(w http.ResponseWriter) {
	responseData := map[string]any{
		"verification_post": false,
	}
	jsonResponse, _ := json.Marshal(responseData)
	_, _ = w.Write(jsonResponse)
}

func (vu VerifyUser) SetResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
}

func NewVerifyUserHandler() *VerifyUser {
	return &VerifyUser{}
}
