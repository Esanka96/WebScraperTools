import enchant

# Create an English dictionary
dictionary = enchant.Dict("en_US")

# Check if a word is valid
word = "substances or"
if dictionary.check(word):
    print(f"'{word}' is a valid word.")
else:
    print(f"'{word}' is not a valid word.")
