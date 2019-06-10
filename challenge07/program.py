import sys

firstLine: bool = True
for line in sys.stdin:
    N: int = int(line)
    if N == 0:
        break
    # Hacky way of not printing a newline after the last line of output
    if not firstLine:
        print("")
    firstLine = False
    solutions: bool = False
    # Go through every possible five digit number, from 01234 to 99999
    for i in range(1234, 99999):
        denominator: str = "{:05d}".format(i)
        numerator: str = ""
        # If the numerator would be over 5 digits, break
        if N * i > 99999:
            break
        numerator = "{:05d}".format(i * N)
        # Make sure that the numerator and denominator have ten unique digits
        if len(set(numerator + denominator)) == 10 and len(numerator) == 5:
            solutions = True
            print("{0} / {1} = {2}".format(numerator, denominator, N))
    if not solutions:
        print("There are no solutions for {}.".format(N))