import json
import re
import os

USERNAME = re.compile(r'^\w{2,9}$')

BANNER = """ W e l c o m e   t o

   ______        __
  / ____ \ ___  / /__________  _____
 / / __ `// _ \/ __/ ___/ __ \/ ___/
/ / / / //  __/ /_(__  ) /_/ / /__
\/_/ /_/ \___/\__/____/\____/\___/
 \____/

           F r e s h e r s ' 2 0 1 6

"""
def is_valid_username(attempt):
    matched = USERNAME.match(attempt)
    return matched is not None


def taken(username):
    users = ['al']
    return username in users


def is_valid_email(attempt):
    if '@' not in attempt:
        print('I think an email address has an @ in it')
        return False
    else:
        return True

def yes_no(prompt):
    print(prompt, end='')
    response_input = ''
    while response_input not in ['Y', 'N']:
        response_input = input('[Y/N]: ')
    return response_input == 'Y'


def get_username():
    while True:
        attempt = input('your "real" name: ')
        if is_valid_username(attempt):
            username = attempt
            if not taken(attempt):
                recurring = False
                break
            else:

                recurring = yes_no('We already have {name}, are you {name}? '
                                    .format(name=username))
                if recurring:
                    break
                else:
                    print("Sure we'll give it another go")
                    continue
        else:
            print('Nah, username must be 2-9 resonable characters')
    return username, recurring


def get_email():
    while True:
        attempt = input('your email address is: ')
        if '@' in attempt:
            return attempt
        else:
            print("Fairly sure an email address has '@' in it somewhere")


def get_user_details():
    username, recurring = get_username()
    email = get_email()
    return dict(zip(('username', 'email', 'recurring'),
                    (username, email, recurring)))


def signups():
    while True:
        os.system('clear')
        print(BANNER)
        details = get_user_details()

        print('\nSo, to be clear:\n'
              ' username: {}\n'
              ' email   : {}'
              .format(details['username'], details['email']))

        if details['recurring']:
            print("\nAnd you\'re already a member?")

        good = yes_no('\nThis is correct? ')
        if good:
            print("Welcome aboard!" if not details['recurring'] else
                  "Welcome back!")
            input()
        else:
            continue


if __name__ == '__main__':
  signups()
