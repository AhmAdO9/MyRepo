secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count<guess_limit:
     guess_count = guess_count + 1
     guess = int(input("Guess: "))
     if guess == secret_number:
          print(f"you won in your {guess_count} attempt !")
          break
     else :
          print("Try again")
