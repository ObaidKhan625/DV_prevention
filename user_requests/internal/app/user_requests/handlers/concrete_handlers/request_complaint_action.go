package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers"
	"github.com/jackc/pgx/v5"
	"net/http"
)

type RequestComplaintAction struct {
}

func (rca RequestComplaintAction) HandleRequest(w http.ResponseWriter, r *http.Request) {
	//TODO implement me
	panic("implement me")
}

func (rca RequestComplaintAction) ExistsInDB(recipientUserId string, actorUserId string, conn *pgx.Conn) bool {
	//TODO implement me
	panic("implement me")
}

func (rca RequestComplaintAction) AddToDB(recipientUserId string, actorUserId string, conn *pgx.Conn) error {
	//TODO implement me
	panic("implement me")
}

func (rca RequestComplaintAction) GetFromDB() []handlers.UserRequest {
	//TODO implement me
	panic("implement me")
}

func (rca RequestComplaintAction) SetUnsuccessfulResponseOnWriter(w http.ResponseWriter) {
	//TODO implement me
	panic("implement me")
}

func (rca RequestComplaintAction) SetResponseOnWriter(w http.ResponseWriter) {
	//TODO implement me
	panic("implement me")
}

func NewRequestComplaintActionHandler() *RequestComplaintAction {
	return &RequestComplaintAction{}
}
