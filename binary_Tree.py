# 7-12-22
# binary tree
#Creating binary tree
# from given list
from binarytree import build


# List of nodes
nodes =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
	binary_tree)

# Getting list of nodes from
# binarytree
print('\nList from binary tree :',
	binary_tree.values)
