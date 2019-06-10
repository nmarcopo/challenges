from typing import List
import sys
import bisect

for line in sys.stdin:
    # Every two lines is a new group of girls
    # Convert list of strings to ints
    gold: List[int] = list(map(int, line.split()))
    blue: List[int] = list(map(int, sys.stdin.readline().split()))
    gold.sort()
    blue.sort()
    smallerGirls: List[int]
    for blueGirl in blue:
        # use bisect to find the index of where the blueGirl would be in the gold list.
        # If the value is 0, we know that the blueGirl is shorter than all of the gold girls left
        blueGirlInGold: int = bisect.bisect_left(gold, blueGirl)
        if blueGirlInGold == 0:
            break
        else:
            gold.remove(gold[blueGirlInGold-1])
    # If there's no gold girl's left, we've fit all of the blue girls
    if gold == []:
        print("Yes")
    else:
        print("No")