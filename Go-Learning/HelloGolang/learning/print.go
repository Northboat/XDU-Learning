package learning

import "fmt"

func SayHello() string {
	return "nmsl"
}

func SayHelloAgain() string {
	return "wdnmd"
}

func TestPrint() {
	fmt.Println("Start TestPrint():")
	num := 18
	str := "hahaha"
	float := 3.14
	char := 'A'
	fmt.Printf("%d, %s, %f, %c\n", num, str, float, char)
	fmt.Printf("%v, %v, %v, %v\n", num, str, float, char)
	fmt.Println("Start TestPrint()!\n")
}
