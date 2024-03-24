package web

import (
	"fmt"
	"log"
	"net/http"
)

func Start() {
	r := initRoutes()
	log.Println("Server started on :8081")
	err := http.ListenAndServe(":8081", r)
	if err != nil {
		fmt.Println("Error")
		return
	}
}
