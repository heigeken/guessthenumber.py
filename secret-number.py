import random

print ('guess the number between 1-10')

secret_number = random.randint(1, 10)

while True:
    guess = int(input('your number:'))
    if guess < secret_number:
        print('your number is too small')
    elif guess > secret_number:
        print('your number is too big')
    else:
        print('you guessed the number!')
        break
