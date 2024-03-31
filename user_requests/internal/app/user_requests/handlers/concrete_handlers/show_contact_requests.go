package concrete_handlers

import "net/http"

type ShowContactRequests struct {
}

func (scr ShowContactRequests) HandleRequest(w http.ResponseWriter, r *http.Request) {
}

func NewShowContactRequestsHandler() *ShowContactRequests {
	return &ShowContactRequests{}
}
