'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true
'''

# pseudocode: 
# to check if something is symetrical then we need to find the middle, split it and compare

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):

        # check if tree is empty
        if not root:
            return True

        def is_mirror(node1, node2):
            # if nodes are empty return true
            if not node1 and not node2:
                return True
            # if only one node is empty then they are not symmetrical
            if not node1 or not node2:
                return False
            # gets both the left and write children and checks if they are the same
            if self.isMirror(node1.left, node1.right) and self.isMirror(node2.right, node2.left):
                return True


        return is_mirror(root.left, root.right)
