package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/creation/concrete_handlers/base"
)

type VerifyUser struct {
	*base.BaseHandler
}

func NewVerifyUserHandler(requestInput map[string]string) *VerifyUser {
	columnDataMap := map[string]string{
		"verified_user_id":  base.GetCurrentUserId(),
		"verifying_user_id": base.GetRecipientUserId(requestInput["user_id"]),
	}
	baseHandlerInput := base.Input{
		"verification",
		columnDataMap,
	}
	return &VerifyUser{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
