package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/concrete_handlers/base"
)

type ReportUser struct {
	*base.BaseHandler
}

func NewReportUserHandler() *ReportUser {
	//queryInputMap := map[string]string{
	//
	//}
	baseHandlerInput := base.Input{
		"report",
		"reported_user_id",
		"reporting_user_id",
	}
	return &ReportUser{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
