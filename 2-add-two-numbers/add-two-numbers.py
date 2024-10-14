# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1=[]
        n2=[]
        while l1:
            temp=l1.val
            l1=l1.next
            n1.append(temp)
        while l2:
            temp=l2.val 
            l2=l2.next
            n2.append(temp)
        n1=n1[::-1]
        n2=n2[::-1]
        f1=0
        f2=0
        for i in n1:
            f1=(f1*10)+i
        for i in n2:
            f2=(f2*10)+i
        n=f1+f2
        l=[]
        if n==0:
            l.append(0)
        else:
            while n>0:
                rem=n%10
                n=n//10
                l.append(rem)
        l3=ListNode(0)
        curr=l3
        print(l)
        for i in l:
            temp=ListNode(i)
            curr.next=temp
            curr=curr.next
        return l3.next


        