import sys
from typing import List

def testViability(dist: int, numFlowers: int, potsList: List[int]) -> bool:
    prevPot = 0
    placed = 0
    for pot in potsList:
        # print("pot:",pot)
        # print("prevPot:",prevPot)
        # print("placed:",placed)
        # print("numFlowers:",numFlowers)
        # print("placed==numFlowers:",placed == numFlowers)
        if prevPot is 0:
            prevPot = pot
            placed = 1 # place the first flower
            # print("placing flower in first pot")
        elif placed == numFlowers:
            return True
        else:
            if pot - prevPot - 1 >= dist:
                prevPot = pot
                placed += 1
                # print("placing flower in pot",pot)
    # print(placed)
    # print(numFlowers)
    if placed == numFlowers:
        return True
    else:
        return False

if __name__ == "__main__":
    # line1: str = sys.stdin.readline()
    # suitablePots: int = int(line1.split()[0])
    # numFlowers: int = int(line1.split()[1])

    # if numFlowers is 0 or suitablePots is 0:
        # print(0)
        # sys.exit()

    # Process input
    for line in sys.stdin:
        suitablePots: int = int(line.split()[0])
        numFlowers: int = int(line.split()[1])
        potsList = []
        if numFlowers is 0:
            continue

        for i in range(suitablePots):
            potsList.append(int(sys.stdin.readline()))

        potsList.sort()
        # print(potsList)
        
        result: bool = True
        dist: int = 0
        while result is True:
            prevDist = dist
            dist += 1
            result = testViability(dist, numFlowers, potsList)
        # if prevDist is 0:
            # print(potsList, suitablePots, numFlowers)
        print(prevDist)