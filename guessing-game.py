secret_number = 9
guess_count = 0

while guess_count < 3:
    guess = int(input("Guess the number: "))
    guess_count += 1

    if guess == secret_number:
        print("You won!")
        break
    
else:
    print("Sorry, you failed!")
