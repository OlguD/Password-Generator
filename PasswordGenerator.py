import string
import random

strings = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
total = int(input('How many password do you want to create: '))
where = input('Where do you want to use that password: ').upper()

def create_pass(total):
    global new_pass
    string_list = []
    n = int(input('Kac basamakli sifre olsun: '))
    for a_string in strings:
        string_list.append(a_string)
    i = 0
    while i <= total:
        random_password = random.choices(string_list, k=n)
        new_pass = ''.join(random_password)
        print(f'Your alternative password/s for {where} is: {new_pass}')
        i+=1
        if i == total:
            break
        else:
            new_pass = ''.join(random_password)
            i+=1
create_pass(total)
