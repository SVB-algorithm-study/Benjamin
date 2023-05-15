# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan&id=level-1

# list1, list2 는 노드 하나이다. 다만, next의 값을 가진.
# next를 가진 노드, 그것이 연결 리스트이다.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = cur = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                cur, list1 = list1, list1.next
            else:
                cur.next = list2
                cur, list2 = list2, list2.next
        
        if list1 or list2:
            cur.next = list1 if list1 else list2

        return head.next