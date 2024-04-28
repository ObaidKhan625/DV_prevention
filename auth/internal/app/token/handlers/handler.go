package handlers

import "net/http"

type TokenHandler interface {
	HandleRequest(w http.ResponseWriter, r *http.Request)
}
