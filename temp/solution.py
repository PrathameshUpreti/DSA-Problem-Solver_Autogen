
def sortedSquares(nums):
    # Square each number in the input array
    squared_nums = [num * num for num in nums]
    
    # Sort the array of squared numbers
    squared_nums.sort()
    
    return squared_nums

# Test cases
print(sortedSquares([-4, -1, 0, 3, 10]))  # Expected output: [0, 1, 9, 16, 100]
print(sortedSquares([-7, -3, 2, 3, 11]))  # Expected output: [4, 9, 9, 49, 121]
print(sortedSquares([1, 2, 3, 4, 5]))     # Expected output: [1, 4, 9, 16, 25]
