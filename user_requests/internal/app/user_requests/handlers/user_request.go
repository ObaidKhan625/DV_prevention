package handlers

import (
	"github.com/jackc/pgx/v5"
	"net/http"
)

type UserRequest interface {
	HandleRequest(w http.ResponseWriter, r *http.Request)
	ExistsInDB(recipientUserId string, actorUserId string, conn *pgx.Conn) bool
	AddToDB(recipientUserId string, actorUserId string, conn *pgx.Conn) error
	GetFromDB() []UserRequest
	SetUnsuccessfulResponseOnWriter(w http.ResponseWriter)
	SetResponseOnWriter(w http.ResponseWriter)
}
