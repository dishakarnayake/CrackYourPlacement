class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
            def can_allocate(max_pages):
                students = 1
                curr_pages = 0
                for pages in arr:
                    if curr_pages + pages > max_pages:
                        students += 1
                        curr_pages = 0
                        if students > m:
                            return False
                    curr_pages += pages
                return True
        
            low = max(arr)
            high = sum(arr)
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if can_allocate(mid):
                    res = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return res