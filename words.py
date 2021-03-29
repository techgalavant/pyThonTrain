import sys
from urllib.request import urlopen


def fetch_words(url):
    story = urlopen(url)
    story_words = []
    
    # replace some words - with help from https://www.geeksforgeeks.org/python-replace-words-from-dictionary/
    # replacement words
    swap_dict = {"noisiest" : "loude$t", "everything" : "allthings", "winter" : "Wintear", "for" : "four"}
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            
            # find words to swap from swap_dict
            story_words.append(swap_dict.get(word, word))

            # story_words.append(word)

    story.close()
    story_words[10] = 'Barsha' # just replace the 11th word with 'Barsha'
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
