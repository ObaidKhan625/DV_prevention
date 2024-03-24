package main

import (
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/config"
	"github.com/ObaidKhan625/DV_Prevention/auth/internal/web"
)

func main() {
	config.Init()
	web.Start()
}
