# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp=head
        l=[]
        while temp:
            l.append(temp.val)
            temp=temp.next
        if l==l[::-1]:
            return True
        else:
            return False
            

        