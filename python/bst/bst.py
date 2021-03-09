from random import randint

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root:
            node_parent = None
            temp = self.root
            while temp:
                node_parent = temp
                if node.data <= temp.data:
                    temp = temp.left
                else:
                    temp = temp.right
            if node.data <= node_parent.data:
                node_parent.left = node
            else:
                node_parent.right = node
        else:
            self.root = node

    def remove(self, node):
        pass

    def inorder_traversal(self):
        temp = self.root
        order = []
        order = inorder(temp, order)
        return order

    def preorder_traversal(self):
        temp = self.root
        order = []
        order = preorder(temp, order)
        return order

    def postorder_traversal(self):
        temp = self.root
        order = []
        order = postorder(temp, order)
        return order

    def search_node(self, node):
        pass

    def sort(self):
        self.inorder_traversal()

def inorder(node, order):
    if not node:
        return
    inorder(node.left, order)
    order.append(node.data)
    inorder(node.right, order)
    return order

def preorder(node, order):
    if not node:
        return
    order.append(node.data)
    preorder(node.left, order)
    preorder(node.right, order)
    return order

def postorder(node, order):
    if not node:
        return
    postorder(node.left, order)
    postorder(node.right, order)
    order.append(node.data)
    return order

def construct_tree():
    bst = BST()
    for i in range(10):
        val = randint(0,20)
        node = Node(val)
        bst.add(node)
    print(bst.inorder_traversal())
    print(bst.postorder_traversal())
    print(bst.preorder_traversal())
    return bst


