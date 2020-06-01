''' Tyler Tiedt & Daniel Abrahms
    HW 3 Program
    Solves the Knap sack problem
'''

def main():
  file = open("knapsack.txt", 'r')
  data = file.read().split('\n')
  maxWeight = int(data[0])
  numItems = int(data[1])
  weight = 0
  cost = 0
  indexies = []
  knapsack = []
  #Puts Knap Sack into a array.
  for i in range (2, len(data) - 1, 2):
    knapsack.append(makeKnapSack(data[i], data[i + 1]))
  print(knapsack)
  # Binary shift to create subsets
  for i in range(2 ** numItems):
    binary = format(i, '#06b')[2:]
    cnt = 0
    tmpWeight = 0
    tmpCost = 0
    index = []
    # Reads the 1's form the binary for the subsets
    for c in binary:
      # Computes weight and cost for each subset
      if(c == '1'):
        tmpWeight += knapsack[cnt][0]
        tmpCost += knapsack[cnt][1]
        index.append(str(cnt))
      cnt += 1
    # Assigns the greates cost under specified weight
    if(tmpWeight <= 10 and tmpCost > cost):
      weight = tmpWeight
      cost = tmpCost
      indexies = index
  print('Weight:' + str(weight) + ' Cost:' + str(cost) + ' At ' + str(indexies))
    
def makeKnapSack(weight, cost):
  return [int(weight), int(cost)]

main()
