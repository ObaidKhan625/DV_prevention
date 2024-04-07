package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/creation/concrete_handlers/base"
)

type ReportUser struct {
	*base.BaseHandler
}

func NewReportUserHandler(requestInput map[string]string) *ReportUser {
	columnDataMap := map[string]string{
		"reported_user_id":  base.GetCurrentUserId(),
		"reporting_user_id": base.GetRecipientUserId(requestInput["user_id"]),
	}
	baseHandlerInput := base.Input{
		"report",
		columnDataMap,
	}
	return &ReportUser{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
