# Used to demonstrate inputting values into a list,
# determine which are strings and numbers (ints),
# lowest/highest values,
# sum just the values,
# distinguish unique values.
# with help from
#   https://pynative.com/python-accept-list-input-from-user/
#   https://leetcode.com/problems/sort-an-array/discuss/461394/Python-3-(Eight-Sorting-Algorithms)-(With-Explanation)
#   https://stackabuse.com/python-get-number-of-elements-in-a-list/
#   https://www.w3schools.com/python/python_ref_string.asp
#   and others

import sys
from icecream import ic

# let user input their own values
# userInputs = input('Enter some values separate by a space:\n')


def newList(userValues):
    userInputs = userValues.split()
    ic(userInputs)
    listCount = len(userInputs)
    uniqueCount = len(set(userInputs))
    print("List has", listCount, "values in it.")
    print("There are", uniqueCount, "unique values in the list.")
    minmax(userInputs)
    # Check for numbers only in the list; add logic to detect if string is a negative number
    numberList = [
        s for s in userInputs
        if (s.isdigit() or s[0] == '-' and s[1:].isdigit())
    ]
    print("The numbers in this list are", numberList)

    # wordList = [w for w in userInputs if not w.isdigit()] # this would still show negative numbers in the wordList

    # to remove negative numbers held as strings
    wordList = [
        w for w in userInputs
        if not (w.isdigit() or w[0] == '-' and w[1:].isdigit())
    ]
    ic(wordList)

    sumValues = 0
    for num in range(0, len(numberList)):
        numberList[num] = int(numberList[num]) # have to convert numbers that are strings to integer
        sumValues = sumValues + numberList[num]
    ic(sumValues)
 


def minmax(userInputs):
    print("Lowest value is", min(userInputs))
    print("Highest value is", max(userInputs))


def main(userValues):
    newInputs = newList(userValues)
    #print_items(newInputs)


if __name__ == '__main__':
    main(sys.argv[1])  # passes the user inputs as argv[1]
