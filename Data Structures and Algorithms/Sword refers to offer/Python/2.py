# -*- coding:utf-8 -*-
class Solution:
    # s Դ�ַ���
    def replaceSpace(self, s):
        # write code here
        return '%20'.join(s.split(' '))
        
"""
Python split() ͨ��ָ���ָ������ַ���������Ƭ��������� num ��ָ��ֵ����ָ� num+1 �����ַ���
�﷨��str.split(str="", num=string.count(str)).
		str -- �ָ�����Ĭ��Ϊ���еĿ��ַ��������ո񡢻���(\n)���Ʊ��(\t)�ȡ�
		num -- �ָ������Ĭ��Ϊ -1, ���ָ����С�
���طָ����ַ����б�
�÷�ʵ����
		str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
		print(str.split( ))       # �Կո�Ϊ�ָ��������� \n
		print str.split((' ', 1 ))# �Կո�Ϊ�ָ������ָ�������
		�����['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
		
Python  join() �����ַ������顣���ַ�����Ԫ�顢�б��е�Ԫ����ָ�����ַ�(�ָ���)��������һ���µ��ַ���
�﷨��  'sep'.join(seq)
		sep���ָ���������Ϊ��
		seq��Ҫ���ӵ�Ԫ�����С��ַ�����Ԫ�顢�ֵ�
		������﷨������sep��Ϊ�ָ�������seq���е�Ԫ�غϲ���һ���µ��ַ���
����ֵ������һ���Էָ���sep���Ӹ���Ԫ�غ����ɵ��ַ���
"""

# -*- coding:utf-8 -*-
class Solution:
    # s Դ�ַ���
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')
"""
Python replace() �������ַ����е� old�����ַ����� �滻�� new(���ַ���)�����ָ������������max�����滻������ max ��
�﷨��str.replace(old, new[, max])
		old -- �����滻�����ַ�����
		new -- ���ַ����������滻old���ַ�����
		max -- ��ѡ�ַ���, �滻������ max ��
"""


# -*- coding:utf-8 -*-
class Solution:
    # s Դ�ַ���
    def replaceSpace(self, s):
        # write code here
        s=list(s)
        for i,val in enumerate(s):
            if(val==' '):
                s[i]='%20'
        return ''.join(s)
                        
                
            
            
            
        
        
