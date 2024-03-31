package handlers

import "net/http"

type UserRequest interface {
	HandleRequest(w http.ResponseWriter, r *http.Request)
}
