package controllers

import (
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/app/token/handlers/generate"
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/app/token/handlers/verify"
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/app/token/serve"
	"net/http"
)

func GenerateToken(w http.ResponseWriter, r *http.Request) {
	handler := generate.NewGenerateToken()
	serve.ServeRequest(w, r, handler)
}

func VerifyToken(w http.ResponseWriter, r *http.Request) {
	handler := verify.NewVerifyToken()
	serve.ServeRequest(w, r, handler)
}
