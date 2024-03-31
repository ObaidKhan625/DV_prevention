package main

import (
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/config"
	"github.com/ObaidKhan625/DV_Prevention/user_requests/internal/web"
)

func main() {
	config.Init()
	web.Start()
}
