import sys

for line in sys.stdin:
    # Split stdin into word and sub-word
    word = line.split()[0]
    subWord = line.split()[1]

    minCount = None
    for subLetter in subWord:
        # "count": integer division of the number of times a subLetter is in the word by the
        # number of times subLetter is in subWord. e.g. if there are two "e" characters, you
        # need to account for both of them in the "count"
        count = word.count(subLetter) // subWord.count(subLetter)
        if minCount is None or minCount > count:
            minCount = count
    
    print(minCount)