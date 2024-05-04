import random

def is_valid_alphabet(guess):
    return all(c.isalpha() and len(c) == 1 for c in guess)

# List of words to choose from
words = [
    "loyal", "coral", "baron", "ultra", "tells", "trick", "prick", "dorky", "hello", "retro",
    "apple", "beach", "cloud", "dairy", "early", "flame", "ghost", "happy", "image", "jolly",
    "kayak", "lemon", "magic", "neon", "ocean", "piano", "quiet", "rider", "sunny", "tiger",
    "umbra", "vivid", "wheat", "xerox", "yacht", "zebra", "angry", "baker", "cabin", "dance",
    "eager", "fable", "giant", "happy", "icing", "joker", "karma", "laser", "mango", "noble",
    "olive", "peach", "quilt", "radio", "salsa", "table", "unity", "virus", "waltz", "xenon",
    "yummy", "zebra", "alert", "basic", "candy", "doubt", "elbow", "flute", "grape", "hobby",
    "image", "jelly", "knock", "lemon", "merry", "noble", "ozone", "panda", "quiet", "rider",
    "solar", "taste", "unite", "vital", "waste", "xerox", "yield", "zebra", "amber", "bison",
    "crown", "daisy", "eagle", "frost", "glass", "heart", "ivory", "jumbo", "karma", "lucky",
    "mango", "naval", "oasis", "piano", "quick", "radar", "sandy", "tiger", "ultra", "vivid",
]
# Select a random word
word = random.choice(words)[:5]  # Select only the first 5 letters of the word

# Initialize variables
guesses = 6
correct_letters = ["_" for _ in word]  # Create a list of underscores with the same length as the word
misplaced_letters = []
eliminated_letters = []

# Main game loop
while guesses > 0:
    # Print current status
    print("\nGuesses left     :", guesses)
    print("Currently known in the word  : ", " ".join(correct_letters))
    print("Misplaced letters            : ", " ".join(misplaced_letters))
    print("Eliminated letters           : ", " ".join(eliminated_letters))

    # Get user guess
    guess = input("Enter your guess: ").lower()[:5]  # Only consider the first 5 letters of the guess and convert it to lowercase

    # Check if guess is a valid alphabet
    if not is_valid_alphabet(guess):
        print("Invalid input! Please enter a valid uppercase or lowercase alphabet.")
        continue

    # Check if guess is correct
    if guess == word.lower():  # Convert word to lowercase for comparison
        print("Congratulations! You guessed the word correctly!")
        print("The correct word is:", word.upper())
        break

    # Check each letter in the guess
    for i, letter in enumerate(guess):
        if letter in word.lower():  # Convert word to lowercase for comparison
            if letter == word.lower()[i]:  # Convert word to lowercase for comparison
                if letter.upper() not in correct_letters:  # Check if letter is already present
                    correct_letters[i] = letter.upper()  # Update the correct letter at the corresponding position
                if letter.lower() in misplaced_letters:  # Check if letter is in misplaced_letters list
                    misplaced_letters.remove(letter.lower())  # Remove letter from misplaced_letters
            else:
                if letter.lower() not in misplaced_letters:  # Check if letter is already present
                    misplaced_letters.append(letter.lower())
        else:
            if letter.lower() not in eliminated_letters:  # Check if letter is already present
                eliminated_letters.append(letter.lower())

    # Update guesses count
    guesses -= 1

# If the player ran out of guesses
if guesses == 0:
    print("\nBetter luck next time!")
    print("The correct word was:", word)
