# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            second.next = first
            curr.next = second
            curr= curr.next.next

        return dummy.next

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
temp = ll
while temp:
    print(temp.val,end = " ")
    temp = temp.next
print()

sol = Solution()
head  = sol.swapPairs(ll)
while head:
    print(head.val,end = " ")
    head = head.next