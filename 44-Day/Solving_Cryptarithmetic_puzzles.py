from itertools import permutations

class CryptarithmeticSolver:
    def __init__(self, words, result):
        # Store the words and result
        self.words = words
        self.result = result
        
        # Create a set of all unique characters involved in the puzzle
        self.unique_chars = set("".join(words) + result)
        
        # Ensure there are no more than 10 unique characters
        if len(self.unique_chars) > 10:
            raise ValueError("There are more than 10 unique characters, which is not solvable with digits 0-9.")
        
        # Convert set to list for indexing
        self.unique_chars = list(self.unique_chars)

    def solve(self):
        # Generate all possible permutations of digits for the unique characters
        for perm in permutations('0123456789', len(self.unique_chars)):
            # Create a dictionary to map characters to digits
            char_to_digit = dict(zip(self.unique_chars, perm))
            
            # Check if this particular assignment solves the puzzle
            if self.is_valid_assignment(char_to_digit):
                return char_to_digit
        
        return None  # No solution found

    def is_valid_assignment(self, char_to_digit):
        # Convert words to their numeric equivalents using the character to digit mapping
        word_values = [self.convert_word_to_number(word, char_to_digit) for word in self.words]
        result_value = self.convert_word_to_number(self.result, char_to_digit)
        
        # Check if the sum of word values equals the result value
        return sum(word_values) == result_value

    def convert_word_to_number(self, word, char_to_digit):
        # Convert each character in the word to its corresponding digit
        num_str = ''.join(char_to_digit[c] for c in word)
        
        # Ensure the word does not have leading zeros
        if num_str[0] == '0':
            return None
        
        return int(num_str)

# Example usage
words = ["SEND", "MORE"]
result = "MONEY"

solver = CryptarithmeticSolver(words, result)
solution = solver.solve()

if solution:
    print("Solution found:")
    for char, digit in solution.items():
        print(f"{char} = {digit}")
else:
    print("No solution found.")
