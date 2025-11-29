package repository

import (
	"StudentManagement/model"
	"sort"
)

var students = []model.Student{
	{1, "熊熊", 1},
	{2, "球吊", 1},
	{3, "TM", 1},
	{4, "戴某", 1},
	{5, "兴根", 1},
	{6, "郭某", 1},
	{7, "强哥", 1},
	{8, "彭奇", 1},
}

func Tagging(student model.StudentWithGrades) model.StudentWithSubjectTag {
	return model.StudentWithSubjectTag{
		ID:     student.ID,
		Name:   student.Name,
		Gender: student.Gender,
		Grades: GradesWithSubjectTag(student.Grades),
	}
}

func NilStudentWithSubjectTag() model.StudentWithSubjectTag {
	return Tagging(model.NilStudentWithGrades())
}

func GetStudents() []model.Student {
	return students
}

func GradeStudent(student model.Student, grades map[int]float64) model.StudentWithGrades {
	return model.StudentWithGrades{
		ID:     student.ID,
		Name:   student.Name,
		Gender: student.Gender,
		Grades: grades,
	}
}

func TagStudent(student model.StudentWithGrades) model.StudentWithSubjectTag {
	return model.StudentWithSubjectTag{
		ID:     student.ID,
		Name:   student.Name,
		Gender: student.Gender,
		Grades: GradesWithSubjectTag(student.Grades),
	}
}

func GetStudentsWithGrades() []model.StudentWithGrades {
	var studentsWithGrades = make([]model.StudentWithGrades, len(students))
	for i := 0; i < len(students); i++ {
		studentsWithGrades[i] = model.StudentWithGrades{
			ID:     students[i].ID,
			Name:   students[i].Name,
			Gender: students[i].Gender,
			Grades: GetGrades(students[i].ID),
		}
	}
	return studentsWithGrades
}

func AddStudent(student model.Student) int {
	student.ID = len(students) + 1
	students = append(students, student)
	return student.ID
}

func GetStudentById(id int) model.StudentWithSubjectTag {
	for _, student := range students {
		if student.ID == id {
			return SetGrades(student)
		}
	}
	return NilStudentWithSubjectTag()
}

func GetStudentByName(name string) model.StudentWithSubjectTag {
	for _, student := range students {
		if student.Name == name {
			return SetGrades(student)
		}
	}
	return NilStudentWithSubjectTag()
}

func DeleteStudentById(id int) bool {
	for index, student := range students {
		if student.ID == id {
			students = append(students[:index], students[index+1:]...)
			return true
		}
	}
	return false
}

// 根据科目返回成绩前列学生
// 科目 subject = 0,1,2,3 分别表示总分排名、三科排名、理科排名和文科排名
// 当人数 count 为 0 时，返回完整排名

func GetSortedStudents(subject, count int) []model.StudentWithSubjectTag {
	var students = GetStudentsWithGrades()
	switch subject {
	case 0:
		sort.Slice(students, func(i, j int) bool {
			return model.GetSum(students[i].Grades) > model.GetSum(students[j].Grades)
		})
	case 1:
		sort.Slice(students, func(i, j int) bool {
			return model.GetMainSum(students[i].Grades) > model.GetMainSum(students[j].Grades)
		})
	case 2:
		sort.Slice(students, func(i, j int) bool {
			return model.GetSciSum(students[i].Grades) > model.GetSciSum(students[j].Grades)
		})
	case 3:
		sort.Slice(students, func(i, j int) bool {
			return model.GetLibSum(students[i].Grades) > model.GetLibSum(students[j].Grades)
		})
	}

	var result = make([]model.StudentWithSubjectTag, len(students))
	for i := 0; i < len(students); i++ {
		result[i] = model.StudentWithSubjectTag{
			ID:     students[i].ID,
			Name:   students[i].Name,
			Gender: students[i].Gender,
			Grades: GradesWithSubjectTag(students[i].Grades),
		}
	}

	if count == 0 {
		return result
	}
	return result[0:count]
}

// 返回一个初始化的各科榜单，用于统计最高分

func GetNilTops(subjectsCount int) map[int]model.StudentWithGrades {
	var tops = make(map[int]model.StudentWithGrades, subjectsCount)
	for key, _ := range Subjects {
		tops[key] = model.NilStudentWithGrades()
	}
	return tops
}
