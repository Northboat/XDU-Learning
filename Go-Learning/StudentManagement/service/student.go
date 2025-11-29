package service

import (
	"StudentManagement/model"
	"StudentManagement/repository"
	"strconv"
)

// 返回各科目排名

func GetStudentsSortedByAllSubjects() []model.StudentWithSubjectTag {
	return repository.GetSortedStudents(0, 0)
}

func GetStudentsSortedByMainSubjects() []model.StudentWithSubjectTag {
	return repository.GetSortedStudents(1, 0)
}

func GetStudentsSortedBySciSubjects() []model.StudentWithSubjectTag {
	return repository.GetSortedStudents(2, 0)
}

func GetStudentsSortedByLibSubjects() []model.StudentWithSubjectTag {
	return repository.GetSortedStudents(3, 0)
}

// 统计各科最高分学生

func GetTopStudents() map[string]model.StudentWithSubjectTag {
	var students = repository.GetStudentsWithGrades()
	var tops = repository.GetNilTops(9)
	// 遍历全部学生
	for _, student := range students {
		// 遍历所有科目，若当前学生当前科目大于记录的最高分，则更新该科目最高分学生为当前学生
		for subject, grade := range student.Grades {
			if grade > tops[subject].Grades[subject] {
				tops[subject] = student
			}
		}
	}
	// 将课程编号转化为课程名返回
	var result = make(map[string]model.StudentWithSubjectTag)
	for subject, student := range tops {
		result[repository.GetSubjectTag(subject)] = repository.TagStudent(student)
	}
	return result
}

// 判断传入参数是否为数字，判断是 ID 还是 Name

func isNumeric(s string) (bool, int) {
	num, err := strconv.Atoi(s)
	return err == nil, num
}

func SearchStudent(content string) model.StudentWithSubjectTag {
	flag, num := isNumeric(content)
	if flag {
		return repository.GetStudentById(num)
	} else {
		return repository.GetStudentByName(content)
	}
}

func DeleteStudent(id int) bool {
	return repository.DeleteStudentById(id)
}

func AddStudent(student model.Student, grades map[int]float64) bool {
	addedStu := repository.AddStudent(student)
	addedGrades := repository.AddGrades(student.ID, grades)
	return addedStu > 0 && addedGrades
}
