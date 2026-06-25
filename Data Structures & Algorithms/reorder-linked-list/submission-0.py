# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            # print(slow.val)
        
    
        # now slow is at mid point of the linkedlist
        # now we reverse the second half
        prev = None
        curr = slow.next
        slow.next = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        
        first = head
        second = prev

        while second is not None :
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1


            first = tmp1
            second = tmp2

      
        return 


        
