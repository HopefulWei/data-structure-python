# 二叉树是一种固定数据结构，但是编程里面要自己定义其类

class Node:                     # 定义节点类
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None


class Tree:                # 定义二叉树类，动态二叉树，可根据list自动生成二叉树
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]   # q表示二叉树最上层的根节点
            while True:  # 这本身就表示一个循环，只有某一个节点没有child1，child2才能返回。起始永远是根节点
                pop_node = q.pop(0)  # pop表示删除函数,默认删除列表的最后一个值，q.pop(0)有两个操作，一、q list删除第一个元素；二、q.pop(0)表示被删除的第一个元素；
                if pop_node.left is None:
                    pop_node.left = node
                    return           # while 表示一直循环，只有return才能返回
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]  # q is Node object
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.item)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.item)
        return res

    def preorder(self,root):  # 先序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item

    def inorder(self,root):  # 中序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorder(root.left)
        right_item = self.inorder(root.right)
        return left_item + result + right_item

    def postorder(self,root):  # 后序遍历
        if root is None:
            return []
        result = [root.item]
        left_item = self.postorder(root.left)
        right_item = self.postorder(root.right)
        return left_item + right_item + result

t = Tree()
for i in range(10):
    t.add(i)
print('层序遍历:',t.traverse())
print('先序遍历:',t.preorder(t.root))
print('中序遍历:',t.inorder(t.root))
print('后序遍历:',t.postorder(t.root))

