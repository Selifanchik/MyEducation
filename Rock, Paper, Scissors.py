import random


def r_s_p(comp, user):
    game = comp + user
    if game == 'RS' or game == 'SR':
        return 'R'
    elif game == 'PR' or game == 'RP':
        return 'R'
    elif game == 'PS' or game == 'SP':
        return 'S'


computer_choice = random.choice(('R', 'S', 'P'))
wish = True
while wish:
    print('Computer made a choice. Choose rock - R, paper - P or scissors - S')
    user_choice = input()
    print(f'Computer is {computer_choice}')
    print(f'User is {user_choice}')
    if computer_choice == user_choice:
        print('Standoff!!!')
    else:
        if r_s_p(computer_choice, user_choice) == computer_choice:
            print('Computer is WIN!!!')
        else:
            print('User is WIN!!!')
    print("Let's play again?")
    if input('Enter Yes or No') == 'No':
        wish = False
