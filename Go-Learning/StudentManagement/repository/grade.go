package repository

import (
	"StudentManagement/model"
)

var Subjects = map[int]string{
	1: "语文",
	2: "数学",
	3: "英语",
	4: "物理",
	5: "化学",
	6: "生物",
	7: "政治",
	8: "历史",
	9: "地理",
}

var Grades = []model.Grade{
	{1, 1, 60},
	{2, 1, 60},
	{3, 1, 60},
	{4, 1, 60},
	{5, 1, 60},
	{6, 1, 60},
	{7, 1, 60},
	{8, 1, 60},
	{9, 1, 60},
}

func GradesWithSubjectTag(grades map[int]float64) map[string]float64 {
	gradesWithSubjectTag := make(map[string]float64, len(grades))
	for key, value := range Subjects {
		gradesWithSubjectTag[value] = grades[key]
	}
	return gradesWithSubjectTag
}

func GetSubjectTag(id int) string {
	return Subjects[id]
}

func GetGrades(id int) map[int]float64 {
	var grades = make(map[int]float64, 9)
	for _, grade := range Grades {
		if grade.StudentID == id {
			grades[grade.SubjectID] = grade.Score
		}
	}
	return grades
}

func SetGrades(student model.Student) model.StudentWithSubjectTag {
	return model.StudentWithSubjectTag{
		ID:     student.ID,
		Name:   student.Name,
		Gender: student.Gender,
		Grades: GradesWithSubjectTag(GetGrades(student.ID)),
	}
}

func AddGrades(id int, grades map[int]float64) bool {
	for subject, grade := range grades {
		Grades = append(Grades, model.Grade{
			SubjectID: subject,
			StudentID: id,
			Score:     grade,
		})
	}
	return true
}
