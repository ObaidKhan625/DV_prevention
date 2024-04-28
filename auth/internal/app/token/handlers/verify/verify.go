package verify

import (
	"encoding/json"
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/config"
	"github.com/golang-jwt/jwt"
	"net/http"
)

type Token struct {
}

func (vt *Token) HandleRequest(w http.ResponseWriter, r *http.Request) {
	// TODO: Take from header
	data, err := verifyToken("Obaid")
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
	}
	w.Header().Set("Content-Type", "application/json")
	err = json.NewEncoder(w).Encode(data)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
	}
	w.WriteHeader(http.StatusOK)
}

func verifyToken(tokenString string) (map[string]any, error) {
	decryptedToken, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return config.GetSecretKey(), nil
	})

	if err != nil {
		return map[string]any{}, err
	}

	bruh := decryptedToken.Claims.(jwt.MapClaims)

	return bruh, nil
}

func NewVerifyToken() *Token {
	return &Token{}
}
