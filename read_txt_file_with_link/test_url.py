# Read link1.txt
with open('link1.txt', 'r', encoding='utf-8') as f1:
    list1 = [line.strip() for line in f1 if line.strip()]


# Zip and print pairs
for key1 in list1:
    print(key1.split(",")[0])
