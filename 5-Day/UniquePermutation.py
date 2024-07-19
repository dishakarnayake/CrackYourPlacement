#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        # code here 
         res=[]
         d={}
         def backtrack(i,ls):
             if i==n:
                 if not d.get(tuple(ls)):
                     res.append(ls.copy())
                     d[tuple(ls)]=True
                 return
             for j in range(i,n):
                 ls[i],ls[j]=ls[j],ls[i]
                 backtrack(i+1,arr)
                 ls[i],ls[j]=ls[j],ls[i]
         backtrack(0,arr)
         return sorted(res)
     
obj = Solution()
print(obj.uniquePerms([1,2,3],3))