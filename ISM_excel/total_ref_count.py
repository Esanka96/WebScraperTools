try:
    with open('ref_num.txt', 'r', encoding='utf-8') as file:
        numbers = file.read().strip().splitlines()
except Exception as error:
    print(f"{error}")

unique_numbers = set(numbers)

count_unique = len(unique_numbers)
print("Count of unique numbers:", count_unique)


