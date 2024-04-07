package handlers

import "net/http"

type UserRequestHandler interface {
	HandleRequest(w http.ResponseWriter, r *http.Request)
}
