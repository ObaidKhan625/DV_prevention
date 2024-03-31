package concrete_handlers

import "net/http"

type RequestComplaintAction struct {
}

func (rca RequestComplaintAction) HandleRequest(w http.ResponseWriter, r *http.Request) {
}

func NewRequestComplaintActionHandler() *RequestComplaintAction {
	return &RequestComplaintAction{}
}
