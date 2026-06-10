# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            curr = list1
            list1 = list1.next
        elif list2 and not list1:
            curr = list2
            list2 = list2.next
        else:
            if list1.val <= list2.val:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next

        head = curr

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return head
