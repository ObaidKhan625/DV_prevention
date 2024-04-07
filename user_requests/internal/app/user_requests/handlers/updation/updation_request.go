package updation

import (
	"github.com/jackc/pgx/v5"
	"net/http"
)

type UpdationRequest interface {
	HandleRequest(w http.ResponseWriter, r *http.Request)
	ExistsInDB(conn *pgx.Conn) bool
	AddToDB(conn *pgx.Conn) error
	GetFromDB() []UpdationRequest
	SetUnsuccessfulResponseOnWriter(w http.ResponseWriter)
	SetResponseOnWriter(w http.ResponseWriter)
}
