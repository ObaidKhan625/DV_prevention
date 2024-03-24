package web

import (
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/web/controllers"
	"github.com/gorilla/mux"
)

func initRoutes() (r *mux.Router) {
	r = mux.NewRouter()
	r.HandleFunc("/auth/token", controllers.GenerateToken).Methods("POST")
	return
}
