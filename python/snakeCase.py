# hand written C-like snake_case without fancy python methods

# define ASCII-indexes
A_UPPER = 65
Z_UPPER = 90
#A_LOWER = 65
#Z_LOWER = 122
LOWER_OFFSET = 32


def snake_case(txt_ar):
    copy_txt = [''] * len(txt_ar)

    # C has a null-terminator that would handle this, we have to do this manually
    upper_count = 0
    # copy array and increase size for later
    for i in range(len(txt_ar)):
        if ord(txt_ar[i]) >= A_UPPER and ord(txt_ar[i]) <= Z_UPPER:
            upper_count += 1
        copy_txt[i] = txt_ar[i]

    # debug
    #print(copy_txt)

    upper_index = 0
    for i in range(len(txt_ar) - upper_count):
        char_to_add = copy_txt[i]
        if ord(char_to_add) >= A_UPPER and ord(char_to_add) <= Z_UPPER:
            char_to_add = chr(ord(char_to_add) + LOWER_OFFSET)
            txt_ar[i + upper_index] = '_'
            upper_index += 1

        # don't change the original array while we iterate over it, use the copy as source
        txt_ar[i + upper_index] = char_to_add


# tests

char_ar = ['m', 'a', 'k', 'e', 'S', 'n', 'a', 'k', 'e', 'C', 'a', 's', 'e', ' ', ' ']
snake_case(char_ar)
print('# TEST 1:', ''.join(char_ar) == "make_snake_case")
print('Output:', ''.join(char_ar))  # Output: make_snake_case

char_ar = ['m', 'o', 'r', 'e', ' ', 'S', 'n', 'a', 'k', 'e', ' ']
snake_case(char_ar)
print('# TEST 2:', ''.join(char_ar) == "more _snake")
print('Output:', ''.join(char_ar))  # Output: more _snake

char_ar = ['B', 'l', 'e', 'r', 'g', 'h', ' ']
snake_case(char_ar)
print('# TEST 3:', ''.join(char_ar) == "_blergh")
print('Output:', ''.join(char_ar))  # Output: _blergh

char_ar = ['l', 'O', 'L', ' ', ' ']
snake_case(char_ar)
print('# TEST 4:', ''.join(char_ar) == "l_o_l")
print('Output:', ''.join(char_ar))  # Output: l_o_l
