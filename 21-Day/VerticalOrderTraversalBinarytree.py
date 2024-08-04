from functools import cmp_to_key

# comparator class for compare two elements in sorting to handle the cases which have same y but differ x
# for eg self -> [(1,2), [3,4,..]] where (1,2) pair is (x,y) and [3,4,...] are the values of node that have same (x,y)
class Compare:
    def main(self,elm):
		# comparing the position of y
        if self[0][-1]<elm[0][-1]:
            return -1
        elif self[0][-1]>elm[0][-1]:
            return 1
        else:
			# if position of y is same for both self and elm, compare the position of x -1 represents for smaller and 1 represents for larger
            if self[0][0]<elm[0][0]:
                return -1
            else:
                return 1

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.vot = {}
        self.find(root)
        self.vot = sorted(self.vot.items(),key=cmp_to_key(Compare.main))
        mapp = {}
		# final merge
        for key,value in self.vot:
            mapp[key[-1]] = mapp.get(key[-1],[]) + value
        return list(mapp.values())
    
    
    def find(self,root,x=0,y=0):
		# traversing the root node to get all (x,y) pairs with node values
        if root == None:
            return
        self.vot[(x,y)] = self.insert(self.vot.get((x,y),[]),root.val)
        self.find(root.left,x+1,y-1)
        self.find(root.right,x+1,y+1)
        
        
    def insert(self, arr, elm):
		# function for inserting a value in our map that have same (x,y) while traversing 
        if not arr:
            return [elm]
        for index,curr in enumerate(arr):
            if curr >= elm:
                return arr[:index] + [elm] + arr[index:]
        return arr + [elm]