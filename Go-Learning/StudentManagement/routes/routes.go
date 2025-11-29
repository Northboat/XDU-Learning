package routes

import (
	"StudentManagement/controller"
	"github.com/gin-gonic/gin"
	"net/http"
)

func SetupRouter() *gin.Engine {
	r := gin.Default()

	// 设置模板目录
	r.LoadHTMLGlob("templates/*")

	// 处理静态资源
	//r.Static("/static", "./static")

	// 访问首页
	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.html", gin.H{
			"title":    "首页",
			"username": "北船",
		})
	})

	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	r.GET("/getRank", controller.GetRank)
	r.GET("/getTop", controller.GetTop)
	return r
}
