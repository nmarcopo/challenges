from typing import List
import sys

for line in sys.stdin:
    sequence: List[str] = line.split()
    continuousSequence: List[str] = []
    maxLen: int = 0
    maxSequence: List[str] = []
    # go through the entire sequence
    for fruit in sequence:
        # try to cut the continuousSequence to just after the first instance of a duplicate fruit.
        # Add the fruit on to the end of the sequence
        try:
            continuousSequence = continuousSequence[continuousSequence.index(fruit)+1:]
            continuousSequence.append(fruit)
        # If there is no duplicate fruit, the cut will fail and we can just append the fruit to the sequence
        except:
            continuousSequence.append(fruit)
        # Check if this sequence is the new max sequence
        if len(continuousSequence) > maxLen:
            maxLen = len(continuousSequence)
            maxSequence = continuousSequence
    print("{}:".format(maxLen), ', '.join(maxSequence))