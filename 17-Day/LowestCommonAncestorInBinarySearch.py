class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        temp = root 

        while temp:
            if p.val > temp.val and q.val > temp.val:
                temp = temp.right
            elif p.val < temp.val and q.val < temp.val:
                temp = temp.left
            else:
                return temp