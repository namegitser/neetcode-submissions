# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def MergeTwoSortedLL(l1, l2):
            f,s = l1, l2
            dummy = ListNode(0)
            head = dummy
            while f and s:
                if f.val < s.val:
                    dummy.next = f
                    f = f.next
                else:
                    dummy.next = s
                    s = s.next

                dummy = dummy.next

            if s:
                dummy.next = s

            if f:
                dummy.next = f

            return head.next

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if len(lists) > i+1 else None
                merged.append(MergeTwoSortedLL(list1,list2))

            lists = merged

        return lists[0]
        

                

