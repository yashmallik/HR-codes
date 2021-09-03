# Objective
# Today, we're going further with Binary Search Trees. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right, top to bottom. You are given a pointer,root , pointing to the root of a binary search tree. Complete the levelOrder function provided in your editor so that it prints the level-order traversal of the binary search tree.

# Hint: You'll find a queue helpful in completing this challenge.

# Function Description

# Complete the levelOrder function in the editor below.

# levelOrder has the following parameter:
# - Node pointer root: a reference to the root of the tree
# ---------X---------------X------------------X------------------X-------------------------X----------------------X--------
# --------X-----------------X------------------X-----------------X--------------------------X----------------------X------------------------------------------------------------------------------

    def levelOrder(self,root):
        #Write your code here
        queue = [root]
        while queue:
            out = queue.pop()
            print(out.data, end=" ")
            if out.left:
                queue.insert(0, out.left)
            if out.right:
                queue.insert(0, out.right)
            
            
        
