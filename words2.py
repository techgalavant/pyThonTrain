# Words2.py demonstrates the removal of the inner (nested) loop for fetch_words
# and uses the icecream library on just the swap_dict words

import sys
from urllib.request import urlopen
from icecream import ic

# URL to use http://sixty-north.com/c/t.txt
# URL to try https://ecspan.com/text/lolly1.txt


def fetch_words(url):
    story = urlopen(url)
    story_words = []

    word_count = 0
    swap_number = 0

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            word_count += line_words.count(word)

            # replace every 5th word with a number count
            if word_count % 5 == 0:
                swap_number += 10
                story_words.append(str(swap_number))
            else:  # amend the word to the list
                # use a function to swap out some words in the swap_dict list
                swap_word(word)
                story_words.append(word)

    story.close()

    story_words.append(str(word_count) + " words in this file.")

    return story_words


# function to swap out certain words
# Replaces inner nested loop in fetch_words from words.py
def swap_word(word):
    swap_dict = {
        "noisiest": "loude$t",
        "everything": "allthings",
        "winter": "Wintear",
        "for": "four",
        "it": "IT",
        "needless": "needful",
        "describe": "illustrate",
        "stomach": "guts",
        "tragedies": "tr@gedie$"
    }
    word = swap_dict.get(word, word)
    ic(word)

    return (word)


def print_items(items):
    for item in items:
        #ic(item)
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # passes the url as argv[1]
