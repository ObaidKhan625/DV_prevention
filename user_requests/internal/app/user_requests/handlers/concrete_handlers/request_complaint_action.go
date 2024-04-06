package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/concrete_handlers/base"
)

type RequestComplaintAction struct {
	*base.BaseHandler
}

func NewRequestComplaintActionHandler() *RequestComplaintAction {
	baseHandlerInput := base.Input{
		"complaint_action",
		"requested_user_id",
		"requesting_user_id",
	}
	return &RequestComplaintAction{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
