package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/concrete_handlers/base"
)

type RequestContactInfo struct {
	*base.BaseHandler
}

func NewRequestContactInfoHandler() *RequestContactInfo {
	baseHandlerInput := base.Input{
		"contact_request",
		"requested_user_id",
		"requesting_user_id",
	}
	return &RequestContactInfo{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
