package generate

import (
	"encoding/json"
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/config"
	"github.com/golang-jwt/jwt"
	"net/http"
	"time"
)

type Token struct {
}

func (gt *Token) HandleRequest(w http.ResponseWriter, r *http.Request) {
	// TODO: Take from header
	tokenString, err := createToken("Obaid")
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
	}
	w.Header().Set("Content-Type", "application/json")
	err = json.NewEncoder(w).Encode(`{token: "` + tokenString + `"}`)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
	}
	w.WriteHeader(http.StatusOK)
}

func createToken(username string) (string, error) {
	token := jwt.NewWithClaims(jwt.SigningMethodHS256,
		jwt.MapClaims{
			"username": username,
			"exp":      time.Now().Add(time.Hour * 24).Unix(),
		})
	tokenString, err := token.SignedString(config.GetSecretKey())

	if err != nil {
		return "", err
	}

	return tokenString, nil
}

func NewGenerateToken() *Token {
	return &Token{}
}
