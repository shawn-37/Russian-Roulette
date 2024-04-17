import random
import time

bank = 1000
lives = 3

print("""
Russian Roulette
You have 3 lives
You have 1000 dollars
Choose a number between 1 and 6
1 = 1.1x betted money
2 = 1.3x betted money
3 = 1.8x betted money
4 = 2.5x betted money
5 = 3.5x betted money
6 = 10x betted money
""")

def win(bet, rounds):
    conversions = [1.1, 1.3, 1.8, 2.5, 3.5, 10]
    return bet * conversions[rounds - 1]
    

def roulette():
    round = 1
    while True:
        global bank, lives
        if lives == 0:
            print(f"You have 0 lives left")
            restart = input("Do you want to play again? (yes/no): ")
            if restart.lower() == "yes":
                lives = 3
                bank = 1000
                round = 1
                print("New game started!")
            else:
                print("Game over.")
                return
        if bank == 0:
            print("You lost all your money, Do you want to play again?")
            restart = input("Do you want to play again? (yes/no): ")
            if restart.lower() == "yes":
                lives = 3
                bank = 1000
                round = 1
                print("New game started!")
            else:
                print("Game over.")
                return
        original_lives = lives
        bullet = random.randint(1, 7)
        print(f"Round {round}, Goodluck!")
        time.sleep(1)
        bet = int(input(f"Place your bet, you have {bank} dollars: "))
        time.sleep(0.2)
        rounds = int(input(f"How many rounds do you want to play: "))
        time.sleep(0.2)
        if bet > 0 and bet <= bank:
            bank = bank - bet
            for num in range(1, rounds + 1):
                time.sleep(.3)
                if bullet == num:
                    print("""
    BANG
                          """)
                    time.sleep(1)
                    if bank != 0:
                        print(f"You lost a life and your bet!")
                    lives -= 1
                    break
                else:
                    print("""
    CLICK
                          """)
                    time.sleep(0.3)
                    print(f"The chamber was empty")
        else:
            print(f"Invalid bet, you have {bank} dollars")
        if lives == original_lives:
                print(f"You got lucky this time, you won {win(bet, rounds)} dollars")
                bank = bank + win(bet, rounds)
        round += 1
        


roulette()
