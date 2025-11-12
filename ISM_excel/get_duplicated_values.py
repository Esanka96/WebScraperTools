from collections import Counter

try:
    with open('ref_num.txt', 'r', encoding='utf-8') as file:
        numbers = file.read().strip().splitlines()
except Exception as error:
    print(f"{error}")

number_counts = Counter(numbers)

duplicates = [num for num, count in number_counts.items() if count > 1]

print("Duplicated values:", duplicates)
print()
print("Duplicated count:",len(duplicates))

