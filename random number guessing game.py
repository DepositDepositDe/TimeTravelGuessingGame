import random  

def number_guessing_game():
    while True:  # Run the game indefinitely until the time traveler decides to stop
        secret_number = random.randint(1, 100)
        attempts = 0  

        max_attempts = 10  

        print("Welcome, time traveler, to the Shady Guessing Game!")
        print("You find yourself in a dimly lit shop, facing a mysterious shopkeeper.")
        print("He claims to hold a secret number between 1 and 100. Can you guess it?")

        while attempts < max_attempts:
            guess = int(input("Enter your guess: "))  

            attempts += 1

            if guess < secret_number:
                print("The shopkeeper sneers, 'Too low! Try again.'")
            elif guess > secret_number:
                print("The shopkeeper chuckles, 'Too high! Try again.'")
            else:
                print(f"The shopkeeper's eyes widen in surprise. 'Congratulations, time traveler!")
                print(f"You've guessed the number {secret_number} correctly!'")
                print(f"It took you {attempts} attempts.")
                break  

        if attempts >= max_attempts:
            print(f"The shopkeeper shakes his head. 'Sorry, time traveler.")
            print(f"You've run out of attempts. The number was {secret_number}.'")

        play_again = input("Would you like to challenge the shopkeeper again? (y/n): ").lower()  
        if play_again != 'y':
            break  

if __name__ == "__main__":
    number_guessing_game()
