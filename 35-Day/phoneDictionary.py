#User function Template for python3

class Solution:
    def displayContacts(self, n, contact, s):
        # code here
       
        # Sort contacts to ensure lexicographical order
        contact.sort()
        
        result = []
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            matches = []
            
            # Find all contacts that start with the current prefix
            for entry in contact:
                if entry.startswith(prefix):
                    matches.append(entry)
            
            # If no matches are found, append "0"
            if not matches:
                result.append(["0"])
            else:
                result.append(sorted(set(matches)))
        
        return result