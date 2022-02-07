package main

import "fmt"

func twoSum(nums []int, target int) []int {
	var a int
	var b int

	for i := 0; i < len(nums); i++ {
		for j := i+1; j < len(nums); j++ {
			if n := nums[i] + nums[j]; n == target {
				a, b = i, j
			}
		}
	}

	return []int{a, b}
}

func main() {
	n := []int{2,7,11,15}
	idx := twoSum(n, 9)

	fmt.Println(idx)
}