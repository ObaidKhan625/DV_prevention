package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/read/concrete_handlers/base"
)

type ShowComplaintRequests struct {
	*base.BaseHandler
}

func NewShowComplaintRequestsHandler() *ShowComplaintRequests {
	columnDataMap := map[string]string{
		"user_id": base.GetCurrentUserId(),
	}
	baseHandlerInput := base.Input{
		"complaint_request",
		columnDataMap,
	}
	return &ShowComplaintRequests{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
