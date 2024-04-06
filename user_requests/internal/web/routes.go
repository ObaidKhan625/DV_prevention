package web

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/web/controllers"
	"github.com/gorilla/mux"
)

func initRoutes() (r *mux.Router) {
	r = mux.NewRouter()
	r.HandleFunc("/verify-user", controllers.VerifyUser).Methods("GET")
	r.HandleFunc("/report-user", controllers.ReportUser).Methods("GET")
	return
}
