class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n
    
    # Function to push an integer into stack 1
    def push1(self, x):
        # Check for overflow
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")
    
    # Function to push an integer into stack 2
    def push2(self, x):
        # Check for overflow
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")
    
    # Function to remove an element from top of stack 1
    def pop1(self):
        # Check for underflow
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return -1
    
    # Function to remove an element from top of stack 2
    def pop2(self):
        # Check for underflow
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return -1

# Example usage:
two_stacks = TwoStacks()

# Push elements into both stacks
two_stacks.push1(2)
two_stacks.push1(3)
two_stacks.push2(4)

# Pop elements from both stacks and print them
print(two_stacks.pop1())  # Output: 3
print(two_stacks.pop2())  # Output: 4
print(two_stacks.pop2())  # Output: -1
