package web

import (
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/web/controllers"
	"github.com/gorilla/mux"
)

func initRoutes() (r *mux.Router) {
	r = mux.NewRouter()
	r.HandleFunc("/token", controllers.GenerateToken).Methods("POST")
	r.HandleFunc("/verify", controllers.VerifyToken).Methods("GET")
	return
}
