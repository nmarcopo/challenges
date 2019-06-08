import sys
from typing import List

# Check to see if "numFlowers" flowers can be placed with minimum distance "dist"
def testViability(dist: int, numFlowers: int, potsList: List[int]) -> bool:
    prevPot: int = 0
    placed: int = 0
    for pot in potsList:
        if prevPot is 0:
            prevPot = pot
            placed = 1 # place the first flower
        elif placed == numFlowers:
            return True
        else:
            if pot - prevPot - 1 >= dist:
                prevPot = pot
                placed += 1
    if placed == numFlowers:
        return True
    else:
        return False

if __name__ == "__main__":
    # Process input
    for line in sys.stdin:
        suitablePots: int = int(line.split()[0])
        numFlowers: int = int(line.split()[1])
        potsList: List = []
        if numFlowers is 0:
            continue

        # Add the pots to a python list
        for i in range(suitablePots):
            potsList.append(int(sys.stdin.readline()))

        # sort list
        potsList.sort()
        
        result: bool = True
        dist: int = 0
        # Go through every possible number of spaces between pots, return the one before one that fails
        # That one will be maximum minimum distance between pots
        while result is True:
            prevDist: int = dist
            dist += 1
            result = testViability(dist, numFlowers, potsList)
        print(prevDist)