package main

import (
	"fmt"
	"strconv"
)

func convertToString(x int) string {

	s := ""

	if x < 0 {
		s += "-"
	}

	w := strconv.Itoa(x)
    
	s += w
    
	return w
}

func isPalindrome(x int) bool {
    s := convertToString(x)

	l := 0
	r := len(s) - 1

	for l <= r {
		if s[l] == s[r] {
			l++
			r--
		} else
		{
			return  false
		}
	}

	return  true
}

func main() {

	x := -121

	fmt.Println(isPalindrome(x))

}
