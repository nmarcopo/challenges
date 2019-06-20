from typing import List
import sys
import itertools

OPERATIONS: List[str] = ["+", "-", "*"]

for line in sys.stdin:
    illuminati: bool = False
    elements: List[int] = list(map(int, line.split()))
    elements2: List[str] = line.split()
    # for n elements, there are n-1 operations
    for operationSet in list(itertools.product(OPERATIONS, repeat = len(elements) - 1)):
        if illuminati:
            break
        # go through all of the permutations of the numbers
        for elementsSet in list(itertools.permutations(elements, len(elements))):
            solution: int = elementsSet[0] # solution starts out as just the first element
            for i in range(1, len(elementsSet)):
                if operationSet[i-1] == "+":
                    solution += elementsSet[i]
                elif operationSet[i-1] == "-":
                    solution -= elementsSet[i]
                elif operationSet[i-1] == "*":
                    solution *= elementsSet[i]
            if solution == 13:
                illuminati = True
                break
    if illuminati:
        print("Illuminati!")
    else:
        print("Nothing to see")