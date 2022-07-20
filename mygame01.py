import random

def guessing_game():
    num = random.randint(1,10)
    print(num)
    guess = int(input('Guess a number between 1 and 10: '))
    times = 1
    while guess != num:
        guess = int(input('Guess again: '))
        times += 1
        if times == 3:
            break
    if num == guess:
        print('You win!')
    else:
        print('You lose! The number was', num)

def main():
    guessing_game()

main()
