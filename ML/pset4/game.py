import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            random_int = random.randint(1, n)
            while True:        
                user_guess = (input("Guess: "))

                try:
                    integer = int(user_guess)
                    if integer > random_int:
                        print("Too large!")
                    elif integer < random_int:
                        print("Too small!")
                    else:
                        exit("Just right") 
                except ValueError:
                    pass
        except ValueError:
            pass
            
main()