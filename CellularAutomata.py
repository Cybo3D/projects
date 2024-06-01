from pyray import * 
from bitstring import BitArray
boxwidth = 10 # change this for different block width in pixels
boxamount = 51 # change this for amount of blocks // boxamount*boxwidth = screenwidth
ruleNumber = 18 #change this for different outcome
ruleset = []
RColorRuleset = []
GColorRuleset = []
BColorRuleset = []
grid = [[0]]

def makeGrid():
    global ruleset
    returnGrid = []
    count = 0
    while count < boxamount:
        if(count != boxamount/2-0.5): returnGrid.append(0)
        if(count == boxamount/2-0.5): returnGrid.append(1)
        count = count + 1

    ruleset1 = bin(ruleNumber).replace("0b", "").zfill(8)
    for digit in ruleset1:  # Iterate over each digit in the binary representation
        ruleset.append(int(digit))
    print(ruleset1)

    RColorRuleset1 = bin(ruleNumber).replace("0b", "").zfill(8)
    for digit in RColorRuleset1:  # Iterate over each digit in the binary representation
        RColorRuleset.append(int(digit))
    print(RColorRuleset1)

    GColorRuleset1 = bin(ruleNumber).replace("0b", "").zfill(8)
    for digit in GColorRuleset1:  # Iterate over each digit in the binary representation
        GColorRuleset.append(int(digit))
    print(GColorRuleset1)

    BColorRuleset1 = bin(ruleNumber).replace("0b", "").zfill(8)
    for digit in BColorRuleset1:  # Iterate over each digit in the binary representation
        BColorRuleset.append(int(digit))
    print(BColorRuleset1)


    return returnGrid

grid[0] = makeGrid()
print(ruleset)
init_window(len(grid[0])*boxwidth, 920, "Hello Pyray")

def GetColor(line):
    return line

def GetNextLine(Len):
    newLine = list(grid[Len])  # Create a copy of the line
    index = 0
    for x in grid[Len]:
        left = grid[Len][(index - 1) % len(grid[Len])]
        right = grid[Len][(index + 1) % len(grid[Len])]
        middle = grid[Len][index]

        if (left, middle, right) == (0, 0, 0): 
            newLine[index] = ruleset[7]
        elif (left, middle, right) == (0, 0, 1): 
            newLine[index] = ruleset[6]
        elif (left, middle, right) == (0, 1, 0): 
            newLine[index] = ruleset[5]
        elif (left, middle, right) == (0, 1, 1): 
            newLine[index] = ruleset[4]
        elif (left, middle, right) == (1, 0, 0): 
            newLine[index] = ruleset[3]
        elif (left, middle, right) == (1, 0, 1): 
            newLine[index] = ruleset[2]
        elif (left, middle, right) == (1, 1, 0): 
            newLine[index] = ruleset[1]
        elif (left, middle, right) == (1, 1, 1): 
            newLine[index] = ruleset[0]

        index += 1

    return GetColor(newLine)

while not window_should_close():
    begin_drawing()
    
    gridIndex = 0

    for line in grid:
        lineIndex = 0
        for x in line:
            if x == 0: draw_rectangle(lineIndex*boxwidth, gridIndex*boxwidth, boxwidth, boxwidth, WHITE)
            elif x == 1: draw_rectangle(lineIndex*boxwidth, gridIndex*boxwidth, boxwidth, boxwidth, BLACK)
            elif x == 2: draw_rectangle(lineIndex*boxwidth, gridIndex*boxwidth, boxwidth, boxwidth, BLUE)
            lineIndex += 1
        gridIndex += 1    

    grid.append(GetNextLine(len(grid)-1))

    end_drawing()

close_window()