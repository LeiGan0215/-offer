# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # ���ش�β����ͷ�����б�ֵ���У�����[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ls=[]
        while listNode!=None:
            ls.append(listNode.val)
            listNode=listNode.next
        #return ls.reverse()
        return ls[::-1]
