from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits = None
        head = digits
        carry = 0

        while l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            carry = 0

            if sum >= 10:
                result = sum % 10
                carry = int(sum / 10)
            else:
                result = sum

            if digits == None:
                digits = ListNode(val=result)
                head = digits
            else:
                digits.next = ListNode(val=result)
                digits = digits.next

            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            sum = l1.val + carry
            carry = 0

            if sum >= 10:
                result = sum % 10
                carry = int(sum / 10)
            else:
                result = sum

            if digits == None:
                digits = ListNode(val=result)
                head = digits
            else:
                digits.next = ListNode(val=result)
                digits = digits.next

            l1 = l1.next

        while l2 != None:
            sum = l2.val + carry
            carry = 0

            if sum >= 10:
                result = sum % 10
                carry = int(sum / 10)
            else:
                result = sum

            if digits == None:
                digits = ListNode(val=result)
                head = digits
            else:
                digits.next = ListNode(val=result)
                digits = digits.next

            l2 = l2.next

        if carry > 0:
            digits.next = ListNode(val=carry)

        return head


if __name__ == "__main__":
    # l1 = ListNode(2, ListNode(4, ListNode(3)))
    # l1 = ListNode(2, ListNode(4, ListNode(5)))
    # l1 = ListNode(9, ListNode(9, ListNode(9)))
    # l2 = ListNode(1)
    l1 = ListNode(1)
    l2 = ListNode(9, ListNode(9, ListNode(9)))
    # l2 = ListNode(5, ListNode(6, ListNode(4)))

    s = Solution()
    digits = s.addTwoNumbers(l1, l2)

    while digits != None:
        print(digits.val)
        digits = digits.next
