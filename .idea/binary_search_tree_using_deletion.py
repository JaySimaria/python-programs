# 31-12-22
# binary search tree deletion
## Implement binary search tree deletion function
class Node(object):
    # Initializing to None
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


# Inserting a node in Binary search tree
def insertion(val):
    # Condition if this is a first node then it will be considered as a root
    if (root.data == None):
        print(val, " Inserted as root")
        root.data = val
    # Else part will be executed for all the other insertions
    else:
        # Pointer to move around tree to search for a place of new node
        p = root

        # Creating a new node and writing a value in the data part
        n = Node()
        n.data = val

        # Iterating to search for an appropriate place of new node
        while (1):
            # if val is less than the current node p indicates that new node will be inserted on left subtree
            if (val < p.data):
                if (p.left == None):
                    print(val, " Inserted on left of ", p.data)
                    p.left = n
                    break
                else:
                    p = p.left
            # if val is greater than the current node p indicates that new node will be inserted on right subtree
            else:
                if (p.right == None):
                    print(val, " Inserted on right of", p.data)
                    p.right = n
                    break
                else:
                    p = p.right


def inorder(node):
    if node:
        # Traversing left subtree
        inorder(node.left)
        # Visiting node
        print(node.data)
        # Traversing right subtree
        inorder(node.right)


def deletion(value):
    # If tree is empty
    if (root == None):
        print("Tree is empty")

    # Initializing the pointers to traverse a tree
    p = root
    q = root

    # Searching for a node to be deleted
    while (1):
        if (value > p.data):
            q = p
            p = p.right
        elif (value < p.data):
            q = p
            p = p.left
        else:
            break

    # If the desired node is a leaf node this condition will be true
    if (p.left == None and p.right == None):
        if (q.left == p):
            q.left = None
        else:
            q.right = None
        print("Value deleted from leaf")
        return p.data

    # deletion of node with one child on right
    if (p.left == None and p.right != None):
        print("\ndeleting node having only right subtree")
        if (q.left == p):
            q.left = p.right
        else:
            q.right = p.right
        return p.data

    # Deletion of node with one child on left
    if (p.left != None and p.right == None):
        print("\ndeleting node having only left subtree")
        if (q.left == p):
            q.left = p.left
        else:
            q.right = p.left
        return p.data

    # deletion of node having 2 childs
    if (p.left != None and p.right != None):
        temp = p
        temp1 = p.right
        while (temp1.left != None):
            temp = temp1
            temp1 = temp1.left
    if (temp1 == temp.left):
        print("\ndeleting node having two childs &amp; right subtree")
        temp.left = temp1.right
    else:
        print("\ndeleting node having two childs &amp; Only right node ")
        temp.right = temp1.right
        p.data = temp1.data
        return value


root = Node()
insertion(10)
insertion(5)
insertion(20)
insertion(30)
insertion(25)
insertion(2)

print("Value ", deletion(25), "deleted successfully")
print("Value ", deletion(10), "deleted successfully")