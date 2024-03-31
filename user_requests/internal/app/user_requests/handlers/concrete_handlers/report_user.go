package concrete_handlers

import "net/http"

type ReportUser struct {
}

func (ru ReportUser) HandleRequest(w http.ResponseWriter, r *http.Request) {
}

func NewReportUserHandler() *ReportUser {
	return &ReportUser{}
}
