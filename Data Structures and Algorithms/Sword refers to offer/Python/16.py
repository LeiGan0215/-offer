#         self.next = None
class Solution:
    # ���غϲ����б�
    def Merge(self, pHead1, pHead2):
        # write code here
        if(pHead1==None):
            return pHead2
        if(pHead2==None):
            return pHead1
        if pHead1.val<pHead2.val:
            pHead1.next=self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next=self.Merge(pHead1,pHead2.next)
            return pHead2
