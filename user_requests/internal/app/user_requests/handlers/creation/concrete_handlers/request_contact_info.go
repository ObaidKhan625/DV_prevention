package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/creation/concrete_handlers/base"
)

type RequestContactInfo struct {
	*base.BaseHandler
}

func NewRequestContactInfoHandler(requestInput map[string]string) *RequestContactInfo {
	columnDataMap := map[string]string{
		"requested_user_id":  base.GetCurrentUserId(),
		"requesting_user_id": base.GetRecipientUserId(requestInput["user_id"]),
	}
	baseHandlerInput := base.Input{
		"contact_request",
		columnDataMap,
	}
	return &RequestContactInfo{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
