class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root:
            pass
        else:
            self.root = node


    def remove(self, node):
        pass

    def balance_tree(self):
        pass

    def traverse(self, node, type='inorder'):
        pass

    def return_bb_tree(self,nodes):
        self.root = nodes[0]
        self.root.left = nodes[1]
        self.root.right = nodes[2]
        self.root.right.left = nodes[3]
        self.root.right.right = nodes[4]
        self.root.left.right = nodes[5]
        self.root.left.left = nodes[6]
        return self.root

    def return_ib_tree(self, nodes):
        self.root = nodes[0]
        self.root.right = nodes[1]
        self.root.right = nodes[2]
        self.root.right.right = nodes[3]
        self.root.right.right = nodes[4]
        self.root.right.right = nodes[5]
        return self.root

binary_tree = BT()
nodes = []
for i in range(7):
    nodes.append(Node(i))
# binary_tree.return_bb_tree(nodes)
# print(binary_tree.root.data)
binary_tree.return_ib_tree(nodes)

def check_balanced_bt(root):  #root D
    if not root:
        return True, -1

    left_status, left_height = check_balanced_bt(root.left) #True, -1

    if not left_status:
        return False, 0

    right_status, right_height = check_balanced_bt(root.right) #True, -1

    if not right_status:
        return False, 0

    is_balanced = abs(left_height - right_height) <= 1 # True
    current_height = max(left_height, right_height) + 1 # 0

    return is_balanced, current_height #True, 0



print(check_balanced_bt(binary_tree.root))

