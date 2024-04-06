package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/concrete_handlers/base"
)

type VerifyUser struct {
	*base.BaseHandler
}

func NewVerifyUserHandler() *VerifyUser {
	baseHandlerInput := base.Input{
		"verification",
		"verified_user_id",
		"verifying_user_id",
	}
	return &VerifyUser{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
