from urllib.request import urlopen


def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)


#        if 'it' in story_words:
#          story_words.replace("that")

    story.close()

    for word in story_words:
        print(word)

if __name__ == '__main__':
    fetch_words()
