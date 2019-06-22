import sys

firstLine: bool = True
for line in sys.stdin:
    # print a newline between test cases
    if firstLine:
        firstLine = False
    else:
        print()

    length: int = int(line.split()[0])
    numOnes: int = int(line.split()[1])

    # Check all binary numbers between 0 and len digits filled with 1s
    for i in range(2 ** length):
        # if the binary number contains numOnes 1s, print it out.
        if str(bin(i)).count("1") == numOnes:
            print(str(bin(i))[2:].zfill(length))