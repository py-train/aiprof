# 02_secret_word_game.py
# A small word game for beginners.
# Goal: type a word, and the program gives fun clues about it.

# input() waits for the user to type something.
word = input("Enter a word: ")

# lower() makes the word lowercase.
# This helps us count vowels more reliably.
word = word.lower()

# A function is a reusable block of code.
# This one counts vowels in a word.
def count_vowels(text):
    vowels = "aeiou"
    count = 0

    # We check one letter at a time.
    for letter in text:
        if letter in vowels:
            count = count + 1

    return count

# Another small function.
# It reverses the word using slicing.
def reverse_text(text):
    return text[::-1]

print("\n--- Word Report ---")
print("Your word:", word)
print("Number of letters:", len(word))
print("Starts with:", word[0])
print("Ends with:", word[-1])
print("Reversed:", reverse_text(word))
print("Vowel count:", count_vowels(word))

# A simple condition.
if word == reverse_text(word):
    print("Nice! This word is a palindrome.")
else:
    print("This word is not a palindrome.")

# Try this:
# 1. Enter different words.
# 2. Try a palindrome like 'level' or 'madam'.
# 3. Change the code so it also counts consonants.
# 4. Change the message style or add your own clue.
