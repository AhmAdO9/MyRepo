import random
words= ["panther", "birdie", "moose"]
print("Welcome to the Word_Guessing_Game!")
secret_word = random.choice(words)
Hidden = ""
print(f"hint: {len(secret_word)} letters")

while len(Hidden) != len(secret_word):
        
        guess= input("guess_word: ")
        for char in secret_word:
            if guess in char:
                  print(char)
                  Hidden += guess
            if len(Hidden) == len(secret_word):
                  print(f"{secret_word} \nWon!")
                  break
            else:
                  print("_")

        if guess not in secret_word:
                     print("try again")

            