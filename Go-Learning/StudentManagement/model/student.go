package model

type Student struct {
	ID     int
	Name   string
	Gender int
}

type StudentWithGrades struct {
	ID     int
	Name   string
	Gender int
	Grades map[int]float64
}

type StudentWithSubjectTag struct {
	ID     int
	Name   string
	Gender int
	Grades map[string]float64
}

func GetSum(grades map[int]float64) float64 {
	var sum = 0.0
	for _, grade := range grades {
		sum += grade
	}
	return sum
}

func GetMainSum(grades map[int]float64) float64 {
	var sum = 0.0
	sum += grades[1]
	sum += grades[2]
	sum += grades[3]
	return sum
}

func GetSciSum(grades map[int]float64) float64 {
	var sum = GetMainSum(grades)
	sum += grades[4]
	sum += grades[5]
	sum += grades[6]
	return sum
}

func GetLibSum(grades map[int]float64) float64 {
	var sum = GetMainSum(grades)
	sum += grades[7]
	sum += grades[8]
	sum += grades[9]
	return sum
}

func NilStudentWithGrades() StudentWithGrades {
	return StudentWithGrades{
		ID:     -1,
		Name:   "",
		Gender: -1,
		Grades: map[int]float64{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
	}
}
