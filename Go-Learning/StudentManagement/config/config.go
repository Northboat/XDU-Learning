package config

import (
	"fmt"
	"gopkg.in/yaml.v3"
	"os"
)

type Config struct {
	Server ServerConfig `yaml:"server"`
	MySQL  MySQLConfig  `yaml:"mysql"`
}

type ServerConfig struct {
	Port int    `yaml:"port"`
	Host string `yaml:"host"`
}

type MySQLConfig struct {
	Host     string `yaml:"host"`
	Port     int    `yaml:"port"`
	Username string `yaml:"username"`
	Password string `yaml:"password"`
}

var AppConfig Config

func LoadConfig() {
	file, err := os.ReadFile("config/config.yaml")
	if err != nil {
		panic(fmt.Sprintf("无法加载配置文件: %v", err))
	}
	err = yaml.Unmarshal(file, &AppConfig)
	if err != nil {
		panic(fmt.Sprintf("解析 YAML 失败: %v", err))
	}
}
