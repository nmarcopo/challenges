from typing import List, Tuple
import sys
import operator

# Need to check each position in the grid and its upper, left, and upper-left
for line in sys.stdin:
    if line.rstrip() == '0':
        sys.exit()
    gridSize: int = int(line)
    grid: List[List[int]] = []
    # Add the grid points to a list
    for gridLine in range(gridSize):
        grid.append([int(point) for point in sys.stdin.readline().split()])
    
    # Go through the grid and check possible previous positions
    pathGrid: List[List[Tuple[int, str]]] = []
    for i in range(gridSize):
        pathRow: List[Tuple[int, str]] = []
        for j in range(gridSize):
            possiblePath: List = []
            # Try to add horizontal
            if j > 0:
                possiblePath.append((grid[i][j] + pathRow[j-1][0], 'hori'))
            # Try to add vertical
            if i > 0:
                # print(i, j)
                # print(pathGrid)
                possiblePath.append((grid[i][j] + pathGrid[i-1][j][0], 'vert'))
            # Try to add diagonal
            if i > 0 and j > 0:
                possiblePath.append((grid[i][j] + pathGrid[i-1][j-1][0], 'diag'))
            # Check the for min, it will return the least recently appended min value
            if len(possiblePath) > 0:
                pathRow.append(min(possiblePath, key=operator.itemgetter(0)))
            else:
                pathRow.append((grid[i][j], 'none'))
        pathGrid.append(pathRow)

    minKak: int = 0
    pathList: List[int] = []
    i = gridSize - 1
    j = gridSize - 1
    # Print the last item in the pathGrid - the final number of kakamora
    print(pathGrid[i][j][0])
    # Go backwards through the pathGrid to determine the correct path
    while i != 0 or j != 0:
        pathList.append(grid[i][j])
        if pathGrid[i][j][1] == 'hori':
            j -= 1
        elif pathGrid[i][j][1] == 'vert':
            i -= 1
        elif pathGrid[i][j][1] == 'diag':
            i -= 1
            j -= 1
    pathList.append(pathGrid[0][0][0])
    pathList.reverse()
    print(" ".join(str(point) for point in pathList))