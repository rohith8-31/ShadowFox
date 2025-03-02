import random

# List of words with hints
words_with_hints = [
    ("tajmahal", "Famous Indian monument"),
    ("ganges", "Sacred Indian river"),
    ("cricket", "Popular Indian sport"),
    ("bollywood", "Indian film industry"),
    ("python", "Popular programming language"),
    ("elephant", "Large animal worshipped in India"),
    ("mahatmagandhi", "Father of the Nation in India")
]

# Choose a random word and hint
word, hint = random.choice(words_with_hints)

# Initialize variables
guessed_word = ["_"] * len(word)
lives = 7
guessed_letters = []

# Function to show current word progress
def display_progress():
    print(" ".join(guessed_word))

# Introduction
print("🎉 Welcome to Hangman - Indian Edition!")
print(f"Hint: {hint}")
print(f"The word has {len(word)} letters.")

# Main game loop
while lives > 0 and "_" in guessed_word:
    print("\n" + "-" * 40)
    display_progress()
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Lives remaining: {lives}")
    
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please guess a single valid letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add to guessed letters
    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        print("✅ Correct guess!")
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed_word[idx] = guess
    else:
        print("❌ Wrong guess!")
        lives -= 1

# Check if player won or lost
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Out of lives! The word was:", word)

