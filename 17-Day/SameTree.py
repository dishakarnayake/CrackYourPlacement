class Solution:
    def isSameTree(self, p, q) :
        # Are both p and q None?
        if not p and not q:
            return True

        # Is one of them None?
        if not p or not q:
            return False

        # Are their values different?
        if p.val != q.val:
            return False

        # Recursive call to the next level down
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)