package controller

import (
	"StudentManagement/service"
	"github.com/gin-gonic/gin"
	"net/http"
)

func GetRank(c *gin.Context) {
	// []model.StudentWithSubjectTag
	c.JSON(http.StatusOK, service.GetStudentsSortedByAllSubjects())
}

func GetTop(c *gin.Context) {
	// map[string]model.StudentWithSubjectTag
	c.JSON(http.StatusOK, service.GetTopStudents())
}
