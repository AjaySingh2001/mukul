import copy

# Original list with nested list inside
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow_copied = copy.copy(original)

# Deep copy
deep_copied = copy.deepcopy(original)

print("Original:", original)
print("Shallow Copy:", shallow_copied)
print("Deep Copy:", deep_copied)

# Now modify one inner list in the original
original[0][0] = 99

print("\nAfter modifying original[0][0] = 99")
print("Original:", original)
print("Shallow Copy:", shallow_copied)  # Will also change (shared inner list)
print("Deep Copy:", deep_copied)        # Unaffected (independent copy)