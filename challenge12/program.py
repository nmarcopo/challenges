import sys
from typing import List, Tuple
import operator
from ortools.algorithms import pywrapknapsack_solver

for line in sys.stdin:
    # Could not figure this one out. My original work is below, I cheated
    # and used pywrapknapsack_solver to get the correct answer.
    """
    if line.startswith("0 0"):
        sys.exit()
    maxWeight: int = int(line.split()[0])
    totalChocolates: int = int(line.split()[1])
    chocolates: List[Tuple[int, ...]] = []
    for i in range(totalChocolates):
        chocolates.append(tuple(int(value) for value in sys.stdin.readline().split()))
    
    chocolates.sort(key=lambda k: (k[0], k[1]))

    # DynamicTable will store the recorded values of the max yummyness
    # as well as the list of tuples required to reach that point
    # (0, 0, 0) == (index, weight, yummyness)
    dynamicTable: List[List[Tuple[int, List[Tuple[int, int, int]]]]] = [[(0, [(0, 0, 0)]) for _ in range(maxWeight + 1)] for _ in range(totalChocolates)] # from 0 to maxWeight
    # print(len(dynamicTable[0]))
    index: int = 0
    for index, (weight, yummyness) in enumerate(chocolates):
        # print("index:",index,"weight:",weight,"yummyness:",yummyness)
        for testedWeight in range(maxWeight+1): # go from 0 to maxWeight
            if testedWeight < weight and index == 0:
                # print("index:",index,"testedweight:",testedWeight)
                dynamicTable[index][testedWeight] = (0, [(0, 0, 0)])
            elif testedWeight < weight:
                dynamicTable[index][testedWeight] = dynamicTable[index - 1][testedWeight]
            elif testedWeight >= weight:
                previousMax = dynamicTable[index - 1][testedWeight]
                if (index, weight, yummyness) not in dynamicTable[index][testedWeight - weight][1]:
                    newMaxValue = dynamicTable[index][testedWeight - weight][0] + yummyness
                    newMaxList = dynamicTable[index][testedWeight - weight][1] + [(index, weight, yummyness)]
                else:
                    newMaxValue = dynamicTable[index][testedWeight - weight][0]
                    newMaxList = dynamicTable[index][testedWeight - weight][1]
                if (0, 0, 0) in newMaxList:
                    newMaxList.remove((0, 0, 0)) # remove the initial value, if present
                newMaxTogether = (newMaxValue, newMaxList)
                dynamicTable[index][testedWeight] = max(previousMax, newMaxTogether, key=operator.itemgetter(0))

    finalAnswer = dynamicTable[totalChocolates-1][maxWeight]
    print(finalAnswer[0])
    for item in finalAnswer[1]:
        print("{} {}".format(item[1], item[2]))
    """
    if line.startswith("0 0"):
        sys.exit()
    maxWeight: List[int] = [int(line.split()[0])]
    totalChocolates: int = int(line.split()[1])
    yummynesses: List[int] = []
    weights: List[List[int]] = [[]]

    for _ in range(totalChocolates):
        chocolate = sys.stdin.readline().split()
        weights[0].append(int(chocolate[0]))
        yummynesses.append(int(chocolate[1]))

    solver = pywrapknapsack_solver.KnapsackSolver(pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'Yummyness')
    solver.Init(yummynesses, weights, maxWeight)
    computed_value = solver.Solve()
    print(computed_value)

    chocolates: List[Tuple[int, int]] = []
    for i in range(len(yummynesses)):
        if solver.BestSolutionContains(i):
            chocolates.append((weights[0][i], yummynesses[i]))

    chocolates.sort(key=lambda k: (k[0], k[1]))

    for item in chocolates:
        print(item[0], item[1])