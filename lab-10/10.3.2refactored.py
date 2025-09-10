def find_common(a, b):
    b_set = set(b)
    return [i for i in a if i in b_set]

# Example usage:
print(find_common([1, 2, 3, 4], [3, 4, 4, 5, 6]))  # Output: [3, 4]