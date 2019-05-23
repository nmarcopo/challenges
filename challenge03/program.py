# Create dictionary of LED numbers
LED = {
    "1":
"""   
  |
  |""",
    "2":
""" _ 
 _|
|_ """,
    "3":
""" _ 
 _|
 _|""",
    "4":
"""   
|_|
  |""",
    "5":
""" _ 
|_ 
 _|""",
    "6":
""" _ 
|_ 
|_|""",
    "7":
""" _ 
  |
  |""",
    "8":
""" _ 
|_|
|_|""",
    "9":
""" _ 
|_|
 _|""",
    "0":
""" _ 
| |
|_|""",
    "-":
"""   
 _ 
   """
    }

import sys

# Convert int to LED string
def makeLED(number: int):
    number = str(number)
    rowOne = ""
    rowTwo = ""
    rowThree = ""
    for digit in number:
        # Merge all rows of the multiline digit strings together
        ledArray = LED[digit].split("\n")
        rowOne += ledArray[0]
        rowTwo += ledArray[1]
        rowThree += ledArray[2]
    return rowOne + "\n" + rowTwo + "\n" + rowThree

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.split()
        nums = [] # keep a running list of the numbers entered into the calculator
        operator = ""
        for index, item in enumerate(line):
            if item is "+":
                nums.append(nums.pop() + nums.pop())
            elif item is "-":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 - num2)
            elif item is "*":
                nums.append(nums.pop() * nums.pop())
            elif item is "/":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 // num2)
            elif item is "^":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 ** num2)
            else:
                nums.append(int(item))
        print(makeLED(nums.pop()))