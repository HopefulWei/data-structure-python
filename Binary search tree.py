# encoding: utf-8
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for item in node_list[1:]:
            self.insert(item)

    # 搜索
    def search(self, node, parent, item):
        if node is None:
            return False, node, parent
        if node.item == item:
            return True, node, parent
        if node.item > item:
            return self.search(node.left, node, item)
        else:
            return self.search(node.right, node, item)

    # 插入
    def insert(self, item):
        flag, n, p = self.search(self.root, self.root, item)
        if not flag:
            new_node = Node(item)
            if item > p.item:
                p.right = new_node
            else:
                p.left = new_node

    # 删除
    def delete(self, root, item):
        flag, n, p = self.search(root, root, item)
        if flag is False:
            print("无该关键字，删除失败")
        else:
            if n.left is None:
                if n == p.left:
                    p.left = n.right
                else:
                    p.right = n.right
                del p
            elif n.right is None:
                if n == p.left:
                    p.left = n.left
                else:
                    p.right = n.left
                del p
            else:  # 左右子树均不为空
                pre = n.right
                if pre.left is None:
                    n.item = pre.item
                    n.right = pre.right
                    del pre
                else:
                    next = pre.left
                    while next.left is not None:
                        pre = next
                        next = next.left
                    n.item = next.item
                    pre.left = next.right
                    del p

    def preorder(self, root):  # 先序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item

    def inorder(self, root):  # 中序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + result + right_item

    def postorder(self, root):  # 后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return left_item + right_item + result
if __name__ == "__main__":
    a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
    bst = BST(a)  # 创建二叉查找树
    bst.inorder(bst.root)  # 中序遍历
    print(bst.inorder(bst.root))
    bst.delete(bst.root, 49)
    print(bst.inorder(bst.root))