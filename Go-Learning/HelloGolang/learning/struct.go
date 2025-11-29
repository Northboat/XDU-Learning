package learning

import "fmt"

// 返回一个切片，如果直接返回数组，如[3]int，这样会导致整个数组的复制（并不是指针返回）
// 所以一般都是返回切片，这是一个指针，指向切片的起始位置

// 返回切片
func getSlice() []int {
	//var nums []int
	nums := make([]int, 0)
	nums = append(nums, 1, 2, 3, 4)
	return nums
}

// 返回一个长度为 3 的整型数组，不会使用
func getArray() [3]int {
	return [3]int{1, 2, 3}
}

// 返回一个 map
func getMap() map[string]int {
	//var m map[string]int
	m := map[string]int{}
	m["one"] = 1
	m["two"] = 2
	return m
}

func getMap1() (m map[string]int) {
	m["one"] = 1
	m["two"] = 2
	return
}

func sum() int {
	return sum1(getSlice()...)
}

func sum1(nums ...int) int {
	sum := 0
	for _, value := range nums {
		sum += value
	}
	return sum
}

func sum2(nums []int) int {
	sum := 0
	for _, value := range nums {
		sum += value
	}
	return sum
}

func TestStruct() {
	fmt.Println(sum())
}
