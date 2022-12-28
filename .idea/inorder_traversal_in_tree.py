# 28-12-22
# inorder traversal in tree
class BTNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    def rootNode(self):
        print(self.val)
root = BTNode('A')
root.rootNode()