# Objective
# Today, we're working with Binary Search Trees (BSTs). Check out the Tutorial tab for learning materials and an instructional video!

# Task
# The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, root, pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.


def getHeight(self,root):
        #Write your code here
        if root:
            leftCout = self.getHeight(root.left)
            rightCout = self.getHeight(root.right)
            if leftCout<rightCout:
                return rightCout + 1
            else:
                return leftCout + 1 
            
        else:
            return -1
        
