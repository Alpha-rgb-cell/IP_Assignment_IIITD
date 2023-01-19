import random

words = ["apple", "table", "happy", "water", "light", "phone", "watch", "carrot", "banana", "orange", "candy", "cookie", "sugar", "bread", "butter", "milk", "coffee", "tea", "lemon", "juice", "music", "dance", "sport", "beach", "ocean", "island", "mountain", "forest", "desert", "river", "lake", "stream", "valley", "flower", "garden", "nature", "city", "town", "village", "field", "farm", "barn", "stable", "house", "room", "bed", "pillow"]

random_word = random.choice(words)

tries = 0

while True:
    guess = input("Enter your guess: ")

    if len(guess) != 5:
        print("Invalid guess. Please enter a 5 character word.")
        continue

    tries += 1

    if guess == random_word:
        print("Congratulations! You have guessed the correct word.")
        break

    if tries == 6:
        print("Sorry, you have exceeded the number of tries. The correct word was", random_word)
        break

    correct_place = ""
    correct_chars = ""
    for i in range(5):
        if guess[i] == random_word[i]:
            correct_place += guess[i]
        elif guess[i] in random_word:
            correct_chars += guess[i]
    print("Correct characters in correct places:", correct_place)
    print("Correct characters in wrong places:", correct_chars)