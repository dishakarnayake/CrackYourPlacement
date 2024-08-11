#User function Template for python3

def findMedian(root):
    l=[]
    k=0
    def dfs(root):
        nonlocal l
        nonlocal k
        if not root:
            return 
        dfs(root.left)
        l.append(root.data)
        dfs(root.right)
        mid=len(l)//2
        if len(l)%2!=0:
            k=l[mid]
        elif int((l[mid]+l[mid-1])/2)==((l[mid]+l[mid-1])/2):
            k=int((l[mid]+l[mid-1])/2)
        else:
            k=((l[mid]+l[mid-1])/2)
        return k
    dfs(root)
    return k