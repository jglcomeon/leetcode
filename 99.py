# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        temp = []
        self.DFS(root, temp)
        res = []
        for i in temp:
            res.append(i.val)
        print(res)
        for i in range(1, len(temp)):
            print(temp[i].val, temp[i-1].val)
            if res[i] < res[i-1]:
                print("fff")
                if i + 1 < len(temp) and temp[i].val > temp[i+1].val:
                    temp[i-1].val, temp[i+1].val = temp[i+1].val, temp[i-1].val
                    print("fff")
                else:
                    temp[i-1].val,temp[i].val = temp[i].val, temp[i-1].val
                    print("Ffff")
                break
        res = []
        for i in temp:
            res.append(i.val)
        print(res)

    def DFS(self, root, temp):
        if not root:
            return
        self.DFS(root.left, temp)
        temp.append(root)
        self.DFS(root.right, temp)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    s = Solution()
    s.recoverTree(root)
