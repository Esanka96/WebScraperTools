# numbers = [
#     4223, 270, 460, 4195, 66, 4197, 438, 917, 409, 520, 324, 1210, 396, 255,
#     4149, 3664, 270, 653, 593, 354, 139, 749, 109, 222, 249, 201, 668, 384,
#     443, 212, 3769, 4207, 1404, 1826, 1275, 3674, 1313, 2038, 3748, 1275, 4324, 253
# ]
#
# # Convert to a set to remove duplicates
# unique_numbers = set(numbers)
#
# # Count unique numbers
# count_unique = len(unique_numbers)
# print("Count of unique numbers:", count_unique)

from collections import Counter

numbers = [
    4223, 270, 460, 4195, 66, 4197, 438, 917, 409, 520, 324, 1210, 396, 255,
    4149, 3664, 270, 653, 593, 354, 139, 749, 109, 222, 249, 201, 668, 384,
    443, 212, 3769, 4207, 1404, 1826, 1275, 3674, 1313, 2038, 3748, 1275, 4324, 253
]

# Count occurrences of each number
number_counts = Counter(numbers)

# Extract numbers that appear more than once
duplicates = [num for num, count in number_counts.items() if count > 1]

print("Duplicated values:", duplicates)

