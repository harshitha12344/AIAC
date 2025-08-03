def max_of_three(numbers):
    if len(numbers) != 3:
        raise ValueError("Input list must contain exactly three numbers.")
    return max(numbers)

# Example usage:
nums = [int(x) for x in input("Enter three numbers separated by spaces: ").split()]
print("Maximum number is:", max_of_three(nums))