import os
import urllib.request

# https://github.com/dwyl/english-words
source_url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
raw_word_file = 'temp/wordl_dl.txt'
target_word_file = 'output/world_wordlist.txt'


def do_download(url, dest):
    url_handle = urllib.request.urlopen(url)
    open(dest, 'w').write(url_handle.read().decode('utf-8'))


def get_filtered_words(words, filter_length):
    filtered = []
    for word in words:
        stripped_word = word.strip()
        if len(stripped_word) == filter_length:
            filtered.append(stripped_word)

    return filtered


if not os.path.exists(raw_word_file):
    print('DOWNLOADING FILE')
    do_download(source_url, raw_word_file)
else:
    print('FILE EXISTS, SKIPPING DOWNLOAD')

all_words = open(raw_word_file).readlines()

match_chars = int(input('enter number of chars to filter words:'))
print(match_chars)

open(target_word_file, 'w').writelines(get_filtered_words(all_words, match_chars))
