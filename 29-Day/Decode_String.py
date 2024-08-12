class Solution:
    def decodeString(self, s) :
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
                continue
            
            innerString = ""
            while stack and stack[-1] != '[':
                innerString = stack.pop() + innerString
            stack.pop() # Pop '['
            
            multiplier = ""
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier
            
            stack.append(int(multiplier) * innerString)
        
        return ''.join(stack)