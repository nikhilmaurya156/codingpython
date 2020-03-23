import random
random_number = random.randint(1, 100)
print(random_number)
chance = 5
user_current_chance = 0
name = input('Enter your name' + '::'+' ')
print(name.upper()+' '+'YOU HAVE FIVE CHANCE TO GUESS A NUMBER FROM 1 TO 100')

while user_current_chance < chance :
    try:
        user_current_chance += 1
        user_choice = int(input('CHANCE'+str(user_current_chance)+' '+'GUESS A NUMBER'+' '))
        if user_choice < random_number:
            print('HINT: '+'Your entered number is smaller')
        elif user_choice > random_number:
            print('HINT: ' + 'Your entered number is bigger')
        else:
            print('Congratulation you have the guess the number right in only ' + str(user_current_chance)+'guess!!')
            break
    except ValueError:
        print('IS NOT NUMBER PLEASE ENTER A NUMBER')