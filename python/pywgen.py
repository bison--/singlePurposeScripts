import string
import secrets
import random

OWN_SPECIAL_CHARACTERS = "_-#"
AVAILABLE_CHARACTERS = string.ascii_letters + string.digits + OWN_SPECIAL_CHARACTERS
pw_length = 42


def create_pw(_pw_length):
    final_pw = []

    count_numbers = 0
    count_letters = 0
    count_special = 0

    for i in range(_pw_length):
        new_character = secrets.choice(AVAILABLE_CHARACTERS)
        final_pw.append(new_character)

        if new_character.isalpha():
            count_letters += 1
        elif new_character.isdigit():
            count_numbers += 1
        else:
            count_special += 1

    if not count_letters:
        final_pw[random.randint(0, _pw_length - 1)] = secrets.choice(string.ascii_letters)
    if not count_numbers:
        final_pw[random.randint(0, _pw_length - 1)] = secrets.choice(string.digits)
    if not count_special:
        final_pw[random.randint(0, _pw_length - 1)] = secrets.choice(OWN_SPECIAL_CHARACTERS)

    count_numbers = 0
    count_letters = 0
    count_special = 0

    for character in final_pw:
        if character.isalpha():
            count_letters += 1
        elif character.isdigit():
            count_numbers += 1
        else:
            count_special += 1

    print("letters:", count_letters, "numbers:", count_numbers, "special:", count_special)

    print("".join(final_pw))

for i in range(10):
    create_pw(pw_length)
