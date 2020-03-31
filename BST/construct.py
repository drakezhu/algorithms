'''
Construct method with preorder array and inorder array
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        idx_dict = {val:ind for ind, val in enumerate(inorder)}
        
        def helper(left, right):
            if left > right: return None
            
            val = preorder.pop(0)
            root = TreeNode(val)
            
            idx = idx_dict[val]
            root.left = helper(left, idx-1)
            root.right = helper(idx+1, right)
            
            
            return root
        
        return helper(0, len(preorder)-1)
