
print('HOME TOUR')
intro = 'You find yourself walking down an empty stree, You\n' \
        'see an empty house. Something moved in a window!\n' \
        'It is dark and you are all alone, you have this urge\n' \
        'to check it out....but do you really want to risk it\n' \
        'for the biscut? The choice is yours\n'
print(intro)

enter_house = input(str('Do you enter the house or running away cause you got better things to do?:\n'
                        'type enter or nope: '))

start_game = 'enter' if enter_house == 'enter' else 'nope'

if start_game == 'nope':
        print('Good choice, I would not want to go there as well.')

while start_game == 'yes':
        pass
