#Experiment File

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def removeNthFromEnd(self, head, n):
        len_ll = 0
        temp = head
        while temp:
            len_ll += 1
            temp = temp.next
        
        if n == len_ll:
            return head.next

        eleNum = len_ll - n

        temp = head
        for _ in range(eleNum-1):
            temp = temp.next
        
        temp.next = temp.next.next

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

sol  = Solution()
node = sol.removeNthFromEnd(head, 2)
while node:
    print(node.val)
    node = node.next