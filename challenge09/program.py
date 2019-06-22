from typing import List, Dict
import sys
from math import ceil

for line in sys.stdin:
    # print(line.rstrip())
    bricks: Dict[int, int] = {}
    bricks[1] = int(line.split()[0]) # 1x1 bricks
    bricks[2] = int(line.split()[1]) # 2x1 bricks
    bricks[3] = int(line.split()[2]) # 3x1 bricks
    bricks[4] = int(line.split()[3]) # 4x1 bricks
    
    # initialize rows as the number of 4x1 bricks
    rows: int = bricks[4]
    
    # Go through 3x1 bricks
    for brick in range(bricks[3]):
        if bricks[1] > 0:
            rows += 1 # add one complete row of legos
            # we've made a complete row of 4, we now remove a 1x1 brick from the available ones
            bricks[1] -= 1
        else:
            rows += 1 # add one incomplete row of legos
    
    # Go through 2x1 bricks
    for brick in range(bricks[2]):
        if bricks[2] >= 2:
            rows += 1 # add one complete row of legos
            bricks[2] -= 2 # we used 2 bricks, remove them from the available ones
        elif bricks[1] >= 2 and bricks[2] > 0:
            rows += 1 # add one complete row of legos
            # we've made a complete row of 4, remove 2 1x1 bricks and 1 2x1 brick from available ones
            bricks[2] -= 1
            bricks[1] -= 2
        elif bricks[1] > 0 and bricks[2] > 0:
            rows += 1 # add one complete row of legos
            bricks[2] -= 1
            bricks[1] -= 1
        elif bricks[2] > 0:
            rows += bricks[2]
            bricks[2] = 0
            break

    # Go through 1x1 bricks
    rows += ceil(bricks[1] / 4) # if we have a decimal, we know that we need 1 extra row
    
    print(rows)