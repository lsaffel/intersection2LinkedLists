# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # store all 'next' pointers from the headA linked list into in a list
        # go through each pointer in headB one by one and see if it's in the list
        # if a common pointer is found, return that pointer
        # else return None

        a_pointer_list = []
        a_ptr = headA   # initialize

        while a_ptr is not None:
            a_pointer_list.append(a_ptr)
            a_ptr = a_ptr.next
        
        # now, a_pointer_list contains all 'next' pointers in the linked list at headA

        b_ptr = headB   # initialize

        # check if each pointer in the linked list at headB is in a_pointer_list
        while b_ptr is not None:

            # see if that pointer is in the list from A. If so, return that pointer
            if b_ptr in a_pointer_list:
                return b_ptr
            # otherwise, the common pointer is not yet found, so look at the next node in the linked list starting at headB
            b_ptr = b_ptr.next

        # we reach this point if b_ptr is None, so we have gone through all of
        # the nodes in linked list b without finding that b pointer 
        # in linkled list A, which are contained in the list a_pointer_list
        return None
      
