# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        def merge(a, b):
            head = ListNode(None)
            li = head
            while a and b:
                if a.val < b.val:
                    li.next = a
                    a = a.next
                else:
                    li.next = b
                    b = b.next
                li = li.next
            if a:
                li.next = a
            if b:
                li.next = b
            return head.next

        while len(lists) > 1:
            st1 = lists.pop()
            st2 = lists.pop()
            node = merge(st1, st2)
            lists.append(node)

        return lists.pop()