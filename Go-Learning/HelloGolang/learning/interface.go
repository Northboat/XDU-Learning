package learning

import "fmt"

// 定义一个接口

type Speaker interface {
	Speak() string
	Run() string
}

// 定义一个结构体

type Animal struct {
	Name string
	Type string
}

// 让 Dog 实现 Speaker 接口

func (d Animal) Speak() string {
	return "I'm " + d.Name + ", I'm a " + d.Type
}

func (d Animal) Run() string {
	return "The " + d.Type + " " + d.Name + " is running"
}

func TestInterface() {
	var s Speaker
	s = Animal{Name: "Buddy", Type: "Dog"} // Dog 自动实现了 Speaker 接口
	fmt.Println(s.Speak())                 // Woof! I'm Buddy
	fmt.Println(s.Run())
}
