#!/usr/bin/python3
import sys

next(sys.stdin) # Skip first line, we don't need to know how many there are
for index, line in enumerate(sys.stdin, 1):
    line = line.rstrip()
    # Process input as integer
    try:
        num = int(line)
    except ValueError:
        print("Error, input was not an integer.", file=sys.stderr)
        sys.exit()

    line = list(map(int, list(line))) # process number as a list to change individual digits
    # Check if number is tidy, go from least significant digit to most significant
    for i in range(len(line) - 1, -1, -1):
        try:
            if line[i] > line[i+1]:
                # if more significant number was higher than less significant number,
                # decrease by 1 and change all less significant numbers to 9
                line[i] -= 1
                for j in range(i+1, len(line)):
                    line[j] = 9
        except IndexError: # if index is out of bounds
            pass
    print("Deck #" + str(index) + ": " + "".join(map(str, line)).lstrip('0')) # remove leading 0s