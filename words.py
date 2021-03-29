import sys
from urllib.request import urlopen


def fetch_words(url):
    story = urlopen(url)
    story_words = []
    
    # replacement words - with help from https://www.geeksforgeeks.org/python-replace-words-from-dictionary/
    swap_dict = {"noisiest" : "loude$t", "everything" : "allthings", "winter" : "Wintear", "for" : "four", "it" : "IT"}
    word_count = 0
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            word_count += line_words.count(word)
            
            # replace every 5th word with "Barsha"
            def replace_words(word):
                if word_count % 5 == 0:
                    story_words.append("Barsha")
                else:
                    # find words to swap from swap_dict
                    story_words.append(swap_dict.get(word, word))

            replace_words(word)

            # story_words.append(word)

    story.close()
    
    story_words.append(str(word_count) + " words in this file.")

    return story_words

def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
