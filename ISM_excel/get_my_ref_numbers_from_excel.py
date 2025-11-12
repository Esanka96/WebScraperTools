file1 = "my_ref_num.txt"
file2 = "ref_num.txt"

with open(file1, "r") as f1:
    my_refs = set(int(line.strip()) for line in f1 if line.strip())

with open(file2, "r") as f2:
    ref_nums = set(int(line.strip()) for line in f2 if line.strip())

common_refs = sorted(my_refs & ref_nums)

if common_refs:
    print("Common reference numbers found:", common_refs)
else:
    print("No matching reference numbers found.")

with open("matched_refs.txt", "w") as out:
    for num in common_refs:
        out.write(f"{num}\n")

print("Total count:",len(common_refs))
print("Matching numbers saved to matched_refs.txt")

