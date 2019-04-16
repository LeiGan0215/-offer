# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # ���ؾ������ĸ��ڵ�
    def Mirror(self, root):
        # write code here
        if root==None:
            return None
        left=root.left
        right=root.right
        root.left=self.Mirror(right)
        root.right=self.Mirror(left)
        return root
        
        
