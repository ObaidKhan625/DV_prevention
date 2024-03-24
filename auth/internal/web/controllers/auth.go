package controllers

import (
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/app/token"
	"net/http"
)

func GenerateToken(w http.ResponseWriter, r *http.Request) {
	token.ProcessRequest(w, r)
}
