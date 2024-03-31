package controllers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/concrete_handlers"
	"net/http"
)

func VerifyUser(w http.ResponseWriter, r *http.Request) {
	handler := concrete_handlers.NewVerifyUserHandler()
	user_requests.ServeRequest(w, r, handler)
}

func ReportUser(w http.ResponseWriter, r *http.Request) {
	handler := concrete_handlers.NewReportUserHandler()
	user_requests.ServeRequest(w, r, handler)
}

func RequestContactInfo(w http.ResponseWriter, r *http.Request) {
	handler := concrete_handlers.NewRequestContactInfoHandler()
	user_requests.ServeRequest(w, r, handler)
}

func RequestComplaintAction(w http.ResponseWriter, r *http.Request) {
	handler := concrete_handlers.NewRequestComplaintActionHandler()
	user_requests.ServeRequest(w, r, handler)
}

func ShowContactRequests(w http.ResponseWriter, r *http.Request) {
	handler := concrete_handlers.NewShowContactRequestsHandler()
	user_requests.ServeRequest(w, r, handler)
}

func ShowComplaintRequests(w http.ResponseWriter, r *http.Request) {
	handler := concrete_handlers.NewShowComplaintRequestsHandler()
	user_requests.ServeRequest(w, r, handler)
}

func RequestContactInfoAction(w http.ResponseWriter, r *http.Request) {
	handler := concrete_handlers.NewRequestContactInfoActionHandler()
	user_requests.ServeRequest(w, r, handler)
}
