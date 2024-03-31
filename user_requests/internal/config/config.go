package config

import (
	"gopkg.in/yaml.v3"
	"log"
	"os"
)

type configuration struct {
	service  string   `yaml:"service"`
	postgres postgres `yaml:"postgres"`
}

type postgres struct {
	uri string `yaml:"uri"`
}

var selectedConfig configuration

func GetServiceName() string {
	return selectedConfig.service
}

func GetPostgresUri() string {
	return selectedConfig.postgres.uri
}

func Init() {
	environmentProfile := lookupEnv("PROFILE", "dev")
	file, err := os.ReadFile("internal/config/setup/" + environmentProfile + ".yaml")
	if err != nil {
		log.Fatalf("Error reading YAML file: %v", err)
	}
	err = yaml.Unmarshal(file, &selectedConfig)
	if err != nil {
		log.Fatalf("Error unmarshalling YAML: %v", err)
	}
}

func lookupEnv(key string, defaultVal string) string {
	val, ok := os.LookupEnv(key)
	if ok && val != "" {
		return val
	}
	return defaultVal
}
