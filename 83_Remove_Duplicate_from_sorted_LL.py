
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        curr_node = head
        while curr_node:
            if curr_node.next and curr_node.val == curr_node.next.val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return head

#Creating input list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(4)

#solving the problem
sol = Solution()
head_new = sol.deleteDuplicates(head)

#Printing updated list
temp = head_new
while temp:
    print(temp.val)
    temp = temp.next