package learning

import (
	"fmt"
	"time"
)

func TestGoroutine() {
	go TestInterface()
	time.Sleep(3 * time.Second)
}

func TestChannel() {
	ch1 := make(chan int)
	ch2 := make(chan string)

	go func() {
		ch1 <- 42 // 发送数据
	}()

	go func() {
		time.Sleep(1 * time.Second)
		ch2 <- "nmsl"
	}()

	num := <-ch1     // 接收数据
	str := <-ch2     // 会被阻塞 1s
	fmt.Println(num) // 输出 42
	fmt.Println(str) // 输出 nmsl
}
