package main

import (
	"StudentManagement/config"
	"StudentManagement/routes"
	"strconv"
)

func main() {
	config.LoadConfig()
	//fmt.Println(config.AppConfig)

	r := routes.SetupRouter()
	// 启动服务，监听 12345 端口
	r.Run(":" + strconv.Itoa(config.AppConfig.Server.Port))
}
