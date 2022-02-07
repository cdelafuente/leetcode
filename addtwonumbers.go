package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	head := result

	cur1 := l1
	cur2 := l2

	var carry *int

	for cur1 != nil && cur2 != nil {
		sum := cur1.Val + cur2.Val

		if sum > 10 {
			c := sum / 10
			carry = &c
			result.Val = sum % 10

		} else {

		}

		cur1 = cur1.Next
		cur2 = cur2.Next

		result.Next = &ListNode{}
		result = result.Next
	}

	return head
}

func main() {
	l1 := &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3}}}
	l2 := &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4}}}

	sum := addTwoNumbers(l1, l2)

	for sum.Next != nil {
		fmt.Println(sum.Val)
		sum = sum.Next
	}
}
