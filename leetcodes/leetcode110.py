#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：leetcode 
@File    ：leetcode110.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/3/15 7:32 下午 
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isBalanced(root):
    if not root:
        return 0

    left = isBalanced(root.left)
    right = isBalanced(root.right)
    if left == -1 or right == -1:
        return -1

    if abs(left - right) <= 1:
        return max(left, right) + 1
    else:
        return -1


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    print(isBalanced(root))


