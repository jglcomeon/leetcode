'''
@Project ：leetcode 
@File    ：pre_in_post.py
@IDE     ：PyCharm 
@Author  ：jiangganglin
@Email   ：jiangganglin@meituan.com
@Date    ：2022/8/28 11:04 下午 
'''


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_post(preorder, inorder):

    if not preorder or not inorder:
        return None

    root = Tree(preorder[0])
    index = inorder.index(preorder[0])
    root.left = get_post(preorder[1: index+1], inorder[:index])
    root.right = get_post(preorder[index+1:], inorder[index+1:])
    return root


def get_pre(inorder, postorder):
    if not inorder or not postorder:
        return None
    root = Tree(postorder[-1])
    index = inorder.index(postorder[-1])
    root.left = get_pre(inorder[:index], postorder[:index])
    root.right = get_pre(inorder[index+1:], postorder[index:-1])
    return root


def get_in(preorder, postorder):
    if not preorder or not postorder:
        return None
    root = Tree(preorder[0])
    if len(preorder) == 1:
        return root
    index = postorder.index(preorder[1])
    root.left = get_in(preorder[1: index+2], postorder[:index+1])
    root.right = get_in(preorder[index+2:], postorder[index+1:])
    return root


def postorder(root, res):
    if not root:
        return
    postorder(root.left, res)
    postorder(root.right, res)
    res.append(root.val)


def preorder(root, res):
    if not root:
        return
    res.append(root.val)
    preorder(root.left, res)
    preorder(root.right, res)


def inorder(root, res):
    if not root:
        return

    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)


def main():
    # 根据前序中序求后续
    root = get_post([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])
    post = []
    postorder(root, post)
    print(post)

    # 根据后续中序求前续
    root = get_pre([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1])
    pre = []
    preorder(root, pre)
    print(pre)

    # 根据前序后续求中序
    root = get_in([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    in_o = []
    inorder(root, in_o)
    print(in_o)




if __name__ == '__main__':
    main()
