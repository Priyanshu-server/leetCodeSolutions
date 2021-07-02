class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        l3 = ListNode(0)
        l3_head = l3
        while l1 and l2:
        
            if l1.val<l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)       
                l3 = l3.next         
                l2  = l2.next

        while l1:
            l3.next = ListNode(l1.val)
            l3  = l3.next
            l1 = l1.next

        while l2:
            l3.next = ListNode(l2.val)
            l3  = l3.next
            l2 = l2.next


        return l3_head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2  = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

def print_node(node):
    while node:
        print(node.val,end = " ")
        node = node.next

print_node(l1)
print()
print_node(l2)

sol  = Solution()
l3 = sol.mergeTwoLists(l1, l2)
print("\n\n")
print_node(l3)
print()