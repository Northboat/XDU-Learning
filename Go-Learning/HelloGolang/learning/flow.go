package learning

import (
	"fmt"
	"math/rand"
)

func TestIf() {
	fmt.Println("Start TestIf():")

	num := rand.Int() // 取随机数

	if i := num - 3270685733633788717; i > 0 {
		fmt.Println(i, SayHello())
	} else if i < 0 {
		fmt.Println(i, SayHelloAgain())
	} else {
		fmt.Println(i, "阳寿 if")
	}

	fmt.Println("End TestIf()!\n")
}

func TestFor() {
	fmt.Println("Start TestFor():")
	sum := 0
	mul := 1
	for i := 1; i <= 5; i++ {
		sum = Add(sum, i)
		mul = Mul(mul, i)
		fmt.Printf("100/i = %d\n", 100/i)
	}
	fmt.Println(sum, mul)

	//for {
	//	fmt.Println("nmsl")
	//}

	i := 0
	for i < 5 {
		fmt.Println(i)
		i++
	}

	fmt.Println("End TestIf()!\n")
}

func TestSwitch() {
	fmt.Println("Start TestSwitch():")
	day := "Monday"
	switch day {
	case "Monday":
		fmt.Println("Start of the week")
	case "Friday":
		fmt.Println("Weekend is near")
	default:
		fmt.Println("Midweek")
	}
	fmt.Println("Start TestSwitch()!\n")

	switch day {
	case "Saturday", "Sunday":
		fmt.Println("Weekend")
	default:
		fmt.Println("Weekday")
	}

	switch num := 2; num {
	case 1:
		fmt.Println("One")
	case 2:
		fmt.Println("Two")
		fallthrough // 继续执行下一个 case
	case 3:
		fmt.Println("Three")
	case 4:
		fmt.Println("Four")
	}

}
