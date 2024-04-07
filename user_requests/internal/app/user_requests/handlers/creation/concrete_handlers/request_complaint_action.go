package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/creation/concrete_handlers/base"
)

type RequestComplaintAction struct {
	*base.BaseHandler
}

func NewRequestComplaintActionHandler(requestInput map[string]string) *RequestComplaintAction {
	columnDataMap := map[string]string{
		"requested_user_id":  base.GetCurrentUserId(),
		"requesting_user_id": base.GetRecipientUserId(requestInput["user_id"]),
		"complaint_id":       base.GetComplaintId(requestInput["complaint_id"]),
	}
	baseHandlerInput := base.Input{
		"complaint_request",
		columnDataMap,
	}
	return &RequestComplaintAction{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
