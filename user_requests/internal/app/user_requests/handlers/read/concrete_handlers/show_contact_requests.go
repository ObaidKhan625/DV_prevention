package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/read/concrete_handlers/base"
)

type ShowContactRequests struct {
	*base.BaseHandler
}

func NewShowContactRequestsHandler() *ShowContactRequests {
	columnDataMap := map[string]string{
		"user_id": base.GetCurrentUserId(),
	}
	baseHandlerInput := base.Input{
		"contact_request",
		columnDataMap,
	}
	return &ShowContactRequests{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
