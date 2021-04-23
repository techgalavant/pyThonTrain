import sys

DIGIT_MAP = {
    'zero': '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
}

def convert(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x

"""
def main():
    newInputs = newList(userValues)
    #print_items(newInputs)
"""

if __name__ == '__main__':
    main()  # passes the user inputs as argv[1]
