
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def PreOrder(root):
    if not root:
        return
    stack = [root]
    while stack:
        cur = stack.pop()
        print(str(cur.val) + ',')
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)


def InOrder(root):
    
    if not root:
        return
    stack = []
    temp = root
    while stack or temp:
        while temp:
            stack.append(temp)
            temp = temp.left
        if stack:
            cur = stack.pop()
            print(str(cur.val) + ',')
            if cur.right:
                temp = cur.right


def postOrder(root):
    if not root:
        return root
    stack1 = [root]
    stack2 = []
    while stack1:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)

    while stack2:
       print(str(stack2.pop().val) + ',')


if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("=======PreOrder========")
    PreOrder(root)
    print("=======InOrder========")
    InOrder(root)
    print("=======AfterOrder========")
    postOrder(root)
