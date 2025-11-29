package main

import (
	"Go/learning"
	"fmt"
)

//TIP <p>To run your code, right-click the code and select <b>Run</b>.</p> <p>Alternatively, click
// the <icon src="AllIcons.Actions.Execute"/> icon in the gutter and select the <b>Run</b> menu item from here.</p>

func main() {

	s := "Hello Golang!"
	fmt.Println(s)

	//learning.TestPrint()
	//learning.TestIf()
	//learning.TestFor()
	//learning.TestSwitch()
	//learning.TestStruct()
	//learning.TestDto()
	//learning.TestStr()
	learning.TestGoroutine()
	learning.TestChannel()
}
