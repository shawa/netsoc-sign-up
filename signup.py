import json
import re
import os
import time

from collections import OrderedDict

BANNER = """ W e l c o m e   t o

   ______        __
  / ____ \ ___  / /__________  _____
 / / __ `// _ \/ __/ ___/ __ \/ ___/
/ / / / //  __/ /_(__  ) /_/ / /__
\/_/ /_/ \___/\__/____/\____/\___/
 \____/

           F r e s h e r s ' 2 0 1 6

"""

def yes_no(prompt):
    answers = {
            'yes': True, 'y': True,
            'no': False, 'n': False
    }

    text = ''
    print(prompt)
    while not text.lower() in answers:
        text = input(' [y/n] >> ')

    return answers[text.lower()]


def get_email(prompt):
    text = input(prompt)
    while '@' not in text:
        print(' "An email address typically has an `@` in it..."')
        text = input('       >> ')
    return text


def get_user_details():
    user = OrderedDict()

    prompts = (
        ("What's your name?\n       >> ",
         'name',
         input),

        ("What's your email address?\n       >> ",
          'email',
          get_email),

        ("Are you already a member?",
         'renewing',
          yes_no),

        ("Do you want to subscribe to our jobs & internships mailing list?",
         'jobseeker',
          yes_no),
    )

    for prompt_text, key, input_func in prompts:
        response = input_func(prompt_text)
        user[key] = response

    return user


def fmt_details(user):
    l = 60
    details = ('           Name: {name}\n'
               '  Email address: {email}'
               .format(name=user['name'], email=user['email']))
    jobseeker_text = ("  You{}want to receive job & internship emails"
                      .format(' ' if user['jobseeker'] else " don't "))

    renewing_text = ("  You are renewing your membership\n" if user['renewing']
                     else "  You are not already a member\n")

    return ("So, to confirm:\n\n" +
            ("#" * l) + '\n' +
            details + '\n\n' +
            jobseeker_text + '\n' +
            renewing_text +
            ("#" * l) + '\n')




def signups():
    while True:
        os.system('clear')
        print(BANNER)
        user = get_user_details()

        time.sleep(0.125)
        print('\n')
        print(fmt_details(user))
        valid = yes_no("Are **all** of these details correct?")

        if valid:
            sure = yes_no("Are you **sure**?\n(We can't contact you if your email is wrong!!)")
            if sure:
                print(json.dumps(user))
                input()
        else:
            continue



if __name__ == '__main__':
  signups()
