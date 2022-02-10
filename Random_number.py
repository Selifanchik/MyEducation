import random

mystery_number = random.randint(1, 50)
found = False
item = 6
while not found and item > 0:
    attempt = int(input('Enter number from 1 to 50: '))
    if attempt == mystery_number:
        found = True
        print('You guessed!')
    elif attempt > mystery_number:
        item -= 1
        print(f'Mystery number is less {attempt}')
    else:
        item -= 1
        print(f'Mystery number is greater {attempt}')
if not found:
    print(f'You not guessed! Mystery number is {mystery_number}')
