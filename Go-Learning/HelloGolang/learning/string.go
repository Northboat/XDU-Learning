package learning

import (
	"fmt"
	"strings"
	"unicode/utf8"
)

func getStr() (string, string) {
	str1 := `nmsl java wdnmd python wcsn c++`
	str2 := "qnmd golang"
	return str1, str2
}

func getLen(str string) int {
	length := utf8.RuneCountInString(str)
	return length
}

func catStr(str1, str2 string) string {
	return str1 + str2
}

func getChar1(str string, index int) rune {
	//c := byte(str[index])
	return rune(str[index])
}

func getChar2(str string, index int) string {
	return str[index : index+1]
}

func appendChars(original string, chars ...rune) string {
	var builder strings.Builder

	// 预先分配足够空间（可选优化）
	builder.Grow(len(original) + len(chars))

	// 写入原始字符串
	builder.WriteString(original)

	// 逐个追加字符
	for _, c := range chars {
		builder.WriteRune(c)
	}

	return builder.String()
}

func TestStr() {
	str := "我糙你的"
	fmt.Println(getLen(str))

	str1, str2 := getStr()
	fmt.Println(str1)
	fmt.Println(str2)
	fmt.Println(getChar1(str1, 0))
	fmt.Println(getChar2(str1, 0))

	s := "世界"
	fmt.Println(s)
	fmt.Println(len(s))
	fmt.Println(getLen(s))

	var builder strings.Builder
	for i, r := range s {
		if i > 0 {
			builder.WriteString(", ")
		}
		builder.WriteRune(r)
	}
	fmt.Println(builder.String())

	ss := "Hello, Go!"
	sub1 := ss[7:]          // 从索引 7 开始截取
	sub2 := ss[0:5]         // 从 0 截取到 5
	fmt.Println(sub1, sub2) // Go!
}
