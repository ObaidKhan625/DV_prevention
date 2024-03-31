package concrete_handlers

import "net/http"

type RequestContactInfoAction struct {
}

func (rca RequestContactInfoAction) HandleRequest(w http.ResponseWriter, r *http.Request) {
}

func NewRequestContactInfoActionHandler() *RequestContactInfoAction {
	return &RequestContactInfoAction{}
}
