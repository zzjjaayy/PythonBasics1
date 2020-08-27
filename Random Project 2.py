# Guessing Game
# user gets three chances to guess the number, if done, he wins, otherwise he fails.

winningNum = 9
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = input("Guess : ")
    guessInt = int(guess)
    if guessInt == winningNum:
        print("you win!")
        break
else:
    print("Game Over")
