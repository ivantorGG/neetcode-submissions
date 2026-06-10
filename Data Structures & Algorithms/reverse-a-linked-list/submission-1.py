# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rewrite_next(curr, prev):
            if not curr:
                return prev

            tail = rewrite_next(curr.next, curr)
            curr.next = prev

            return tail


        return rewrite_next(head, None)
