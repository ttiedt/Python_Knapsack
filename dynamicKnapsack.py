''' Tyler Tiedt
    HW 4 Program
    Solves the Knap sack problem using dynamic programing
'''
'''
100 items:
  d function: 0.002 seconds
  f function: 0.004 seconds
  f is .002 sec slower
  coverage: ~25%

5 items:
  d function: 0.00064 seconds
  f function: 0.00056 seconds
  f is .00004 sec faster
  coverage: ~18%

So, by this data, the memoization function is better for smaller data sets, and for larger data sets the memoization function is not as good.
I can see this being the case because the number of recursive calls grows exponetial with the size of the data set growing.
The order of growth for memoization is O(2^n) but for a data set of n = 100, my algorithm is not getting anywhere close to 2^100 calls. 2^100
is worst case but for this algoithm im not really sure what data set would give you a 'worse case'.

'''
import time

def makeKnapSack(weight, cost):
  return [int(weight), int(cost)]

def dFunc(knapsack, maxWeight, numItems):
    fTable = []
    for row in range(numItems):
      val = 0
      curRow = []
      for col in range(maxWeight + 1):
        if(col < knapsack[row][0]):
          if(row != 0):
            val = fTable[row - 1][col]     
        else:
          if(row == 0):
            val = knapsack[row][1]
          else:
            val = max(knapsack[row][1] + fTable[row - 1][col - knapsack[row][0]], fTable[row - 1][col])
        curRow.append(val)
      fTable.append(curRow)
    cost = fTable[numItems - 1][maxWeight]
    return fTable, cost

def fFunc(knapsack, maxWeight, numItems):
  if(numItems == 0 or maxWeight == 0):
    return 0
  if(knapsack[numItems-1][0] > maxWeight):
    return fFunc(knapsack, maxWeight, numItems - 1)
  if(lTable[numItems - 1][maxWeight] != float('inf')):
    return lTable[numItems - 1][maxWeight]
  else:
    x = max(knapsack[numItems-1][1] + fFunc(knapsack, maxWeight - knapsack[numItems - 1][0], numItems - 1), fFunc(knapsack, maxWeight, numItems - 1))
    lTable[numItems - 1][maxWeight] = x
    return x

file = open("knapsack_big.txt", 'r')
data = file.read().split('\n')
funct = data[0]
maxWeight = int(data[1])
numItems = int(data[2])
weight = 0
cost = 0
indexies = []
knapsack = []

#Puts Knap Sack into a array.
for i in range (3, len(data) - 1, 2):
  knapsack.append(makeKnapSack(data[i], data[i + 1]))
knapsack = sorted(knapsack)
if(funct == 'd'): 
  t1 = time.time()
  fTable, cost = dFunc(knapsack, maxWeight, numItems)
  t2 = time.time()
  row = numItems - 1
  col = maxWeight
  solution = []
  while(cost != 0):
    if(fTable[row - 1][col] == cost):
      row = row - 1
    elif(fTable[row - 1][col] != cost):
      solution.append(knapsack[row])
      cost = cost - knapsack[row][1]
      col = col - knapsack[row][0]

  cost = fTable[numItems - 1][maxWeight]     
  print('Items:', solution)
  print('Max Value:', cost)
  #print('Time', t2 - t1)
if(funct == 'f'):
  lTable = [[float('inf') for col in range(maxWeight + 1)] for row in range(numItems)]
  t1 = time.time()
  cost = fFunc(knapsack, maxWeight, numItems)
  t2 = time.time()
  row = numItems - 1
  col = maxWeight
  numCells = 0
  usedCells = 0
  for row in range(numItems):
    for col in range(maxWeight + 1):
      numCells = numCells + 1
      if(lTable[row][col] != float('inf')):
        usedCells = usedCells + 1
  print('Table coverage: ', usedCells / numCells)
  solution = []
  while(cost != 0):
    if(lTable[row - 1][col] == cost):
      row = row - 1
    elif(lTable[row - 1][col] != cost):
      solution.append(knapsack[row])
      cost = cost - knapsack[row][1]
      col = col - knapsack[row][0]
  cost = lTable[numItems - 1][maxWeight]     
  print('Items:', solution)
  print('Max Value:', cost)
  #print('Time', t2 - t1)