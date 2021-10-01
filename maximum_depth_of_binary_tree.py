def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    depthL = 1
    depthR = 1
    
    if root.left != None:
        depthL = self.maxDepth(root.left) +1
    if root.right != None:
        depthR = self.maxDepth(root.right) +1
    
    return max(depthL, depthR)