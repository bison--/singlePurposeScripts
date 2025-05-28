from string import ascii_uppercase
from string import digits
from random import choice

ALL_AVAILABLE_CHARACTERS = ascii_uppercase + digits

def generate_fake_steam_key():
    fake_key = ''
    for i_blocks in range(0, 3):
        for i_chars in range(0, 5):
            fake_key += choice(ALL_AVAILABLE_CHARACTERS)

        fake_key += '-'

    return fake_key.strip('-')


for i in range(0, 500):
    print(generate_fake_steam_key())

#print('#' * 10)

#for i in range(0, 100):
#    print('this_is_a_free_game_', i, sep='')
