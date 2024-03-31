package concrete_handlers

import "net/http"

type RequestContactInfo struct {
}

func (rci RequestContactInfo) HandleRequest(w http.ResponseWriter, r *http.Request) {
}

func NewRequestContactInfoHandler() *RequestContactInfo {
	return &RequestContactInfo{}
}
