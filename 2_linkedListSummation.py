class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = carry = 0
        l3Head = ListNode()
        temp3 = l3Head
        temp1 = l1
        temp2 = l2
        while temp1 and temp2:
            sum = temp1.val + temp2.val + carry
            carry = sum //10
            temp3.next = ListNode(sum%10)
            temp1,temp2,temp3 = temp1.next,temp2.next,temp3.next

        l3 = temp1 if temp1 else temp2
        while l3:
            sum = l3.val + carry
            carry = sum //10
            temp3.next = ListNode(sum%10)
            l3,temp3 = l3.next,temp3.next
        if carry >0:
            temp3.next = ListNode(carry)
        
        return l3Head.next


# Initializing Nodes 

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next =  ListNode(9)
l2.next.next.next =  ListNode(9)

# Testing Function 

sol = Solution()
summ = sol.addTwoNumbers(l1,l2)

while summ:
    print(summ.val,end  = " ")
    summ = summ.next
print()