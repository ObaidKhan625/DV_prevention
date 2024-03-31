package concrete_handlers

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"github.com/Masterminds/squirrel"
	"github.com/jackc/pgx/v5"
	"net/http"
)

type VerifyUser struct {
}

func (vu VerifyUser) HandleRequest(w http.ResponseWriter, r *http.Request) {
	vu.setResponseOnWriter(w)

	userIdToBeVerified := r.URL.Query().Get("user_id")
	// todo: Get from auth service
	currentUserId := "1"
	if currentUserId == userIdToBeVerified {
		vu.setUnsuccessfulVerificationOnWriter(w)
		return
	}

	conn, err := pgx.Connect(context.Background(), "postgres://postgres:@localhost/user_request")
	if err != nil {
		fmt.Printf("Unable to connect to database: %v\n", err)
		vu.setUnsuccessfulVerificationOnWriter(w)
		return
	}
	defer conn.Close(context.Background())

	verificationExists := vu.verificationExistsInDB(userIdToBeVerified, conn)
	if verificationExists {
		vu.setUnsuccessfulVerificationOnWriter(w)
		return
	}

	err = vu.addVerificationInDB(userIdToBeVerified, currentUserId, conn)
	fmt.Println("Insert error : ", err)

}

func (vu VerifyUser) verificationExistsInDB(userIdToBeVerified string, conn *pgx.Conn) bool {
	verificationExistsSQL :=
		squirrel.Select("1").
			From("verification").
			Where(squirrel.Eq{
				"verified_user_id":  userIdToBeVerified,
				"verifying_user_id": 1,
			}).
			PlaceholderFormat(squirrel.Dollar).
			Limit(1)

	sql, args, _ := verificationExistsSQL.ToSql()

	resultFlag := 0
	err := conn.QueryRow(context.Background(), sql, args...).Scan(&resultFlag)
	if err != nil && errors.Is(err, pgx.ErrNoRows) {
		return false
	}
	return true
}

func (vu VerifyUser) addVerificationInDB(verifiedUserId string, verifyingUserId string, conn *pgx.Conn) error {
	insertVerificationSQL := squirrel.Insert("verification").
		Columns("verified_user_id", "verifying_user_id").
		Values(verifiedUserId, verifyingUserId)
	sql, args, _ := insertVerificationSQL.ToSql()
	fmt.Println(sql)
	fmt.Println(args)
	_, err := conn.Exec(context.Background(), sql, args...)
	return err
}

func (vu VerifyUser) setUnsuccessfulVerificationOnWriter(w http.ResponseWriter) {
	responseData := map[string]any{
		"verification_post": false,
	}
	jsonResponse, _ := json.Marshal(responseData)
	_, _ = w.Write(jsonResponse)
}

func (vu VerifyUser) setResponseOnWriter(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
}

func NewVerifyUserHandler() *VerifyUser {
	return &VerifyUser{}
}
