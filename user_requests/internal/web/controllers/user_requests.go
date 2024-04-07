package controllers

import (
	creation_handlers "github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/creation/concrete_handlers"
	read_handlers "github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/read/concrete_handlers"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/serve"

	//updation_handlers "github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/updation/handlers/concrete_handlers"
	"net/http"
)

func VerifyUser(w http.ResponseWriter, r *http.Request) {
	requestInput := createHandlerInput(r)
	handler := creation_handlers.NewVerifyUserHandler(requestInput)
	serve.ServeRequest(w, r, handler)
}

func ReportUser(w http.ResponseWriter, r *http.Request) {
	requestInput := createHandlerInput(r)
	handler := creation_handlers.NewReportUserHandler(requestInput)
	serve.ServeRequest(w, r, handler)
}

func RequestContactInfo(w http.ResponseWriter, r *http.Request) {
	requestInput := createHandlerInput(r)
	handler := creation_handlers.NewRequestContactInfoHandler(requestInput)
	// todo: user notifications
	serve.ServeRequest(w, r, handler)
}

func RequestComplaintAction(w http.ResponseWriter, r *http.Request) {
	requestInput := createHandlerInput(r)
	handler := creation_handlers.NewRequestComplaintActionHandler(requestInput)
	// todo: user notifications
	serve.ServeRequest(w, r, handler)
}

func ShowContactRequests(w http.ResponseWriter, r *http.Request) {
	handler := read_handlers.NewShowContactRequestsHandler()
	// todo: notifications 0
	serve.ServeRequest(w, r, handler)
}

func ShowComplaintRequests(w http.ResponseWriter, r *http.Request) {
	handler := read_handlers.NewShowComplaintRequestsHandler()
	// todo: notifications 0
	serve.ServeRequest(w, r, handler)
}

//
//func RequestContactInfoAction(w http.ResponseWriter, r *http.Request) {
//	handler := concrete_handlers.NewRequestContactInfoActionHandler()
//	user_requests.ServeRequest(w, r, handler)
//}

func createHandlerInput(r *http.Request) map[string]string {
	queryParams := r.URL.Query()
	requestInput := make(map[string]string)
	for key, value := range queryParams {
		if len(value) > 0 {
			requestInput[key] = value[0]
		}
	}
	return requestInput
}
