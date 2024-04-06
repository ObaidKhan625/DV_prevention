package concrete_handlers

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/app/user_requests/handlers/concrete_handlers/base"
	"github.com/jackc/pgx/v5"
	"net/http"
)

type ReportUser struct {
	*base.BaseHandler
}

func (ru ReportUser) HandleRequest(w http.ResponseWriter, r *http.Request) {
	ru.BaseHandler.HandleRequest(w, r)
}

func (ru ReportUser) ExistsInDB(userIdToBeReported string, userIdReporting string, conn *pgx.Conn) bool {
	return ru.BaseHandler.ExistsInDB(userIdToBeReported, userIdReporting, conn)
}

func (ru ReportUser) AddToDB(reportedUserId string, reportingUserId string, conn *pgx.Conn) error {
	return ru.BaseHandler.AddToDB(reportedUserId, reportingUserId, conn)
}

func (ru ReportUser) GetFromDB() []handlers.UserRequest {
	return ru.BaseHandler.GetFromDB()
}

func NewReportUserHandler() *ReportUser {
	baseHandlerInput := base.Input{
		"report",
		"reported_user_id",
		"reporting_user_id",
		"report_post",
	}
	return &ReportUser{
		base.NewBaseHandler(
			baseHandlerInput,
		),
	}
}
