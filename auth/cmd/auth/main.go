package main

import (
	"fmt"
	"github.com/golang-jwt/jwt"
	"time"
)

func main() {
	//config.Init()
	//web.Start()
	fmt.Println(createToken("Obaid"))
}

var secretKey = []byte("secret-key")

func createToken(username string) (string, error) {
	token := jwt.NewWithClaims(jwt.SigningMethodHS256,
		jwt.MapClaims{
			"username": username,
			"exp":      time.Now().Add(time.Hour * 24).Unix(),
		})
	tokenString, err := token.SignedString(secretKey)

	if err != nil {
		return "", err
	}

	// Take token from header

	decryptedToken, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return secretKey, nil
	})

	if err != nil {
		return "", err
	}

	bruh := decryptedToken.Claims.(jwt.MapClaims)

	return bruh["username"].(string), nil
}
