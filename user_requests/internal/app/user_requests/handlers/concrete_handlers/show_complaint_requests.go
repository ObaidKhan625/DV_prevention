package concrete_handlers

import "net/http"

type ShowComplaintRequests struct {
}

func (scr ShowComplaintRequests) HandleRequest(w http.ResponseWriter, r *http.Request) {
}

func NewShowComplaintRequestsHandler() *ShowComplaintRequests {
	return &ShowComplaintRequests{}
}
