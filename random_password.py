import random
user = input('Enter username ')
new_pass = ''
ran_var = ''
ran_num = ''
count = 1
for i in user:
    ran_var += random.choice('abcdefghijklmnopqrstuvwxyz')
    ran_num += str(random.randint(0, 9))
    new_pass += i
    if count > 3:
        break
    count = count+1
print('Password is '+new_pass+ran_var+random.choice('!@£$%&')+ran_num)
