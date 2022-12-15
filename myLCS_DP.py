import random
import sys

def myLCS_DP(list1):
  myLetters = ["A", "T", "C", "G"]
  n = len(list1)
  if n == 1:
    myString1 = ''.join(random.choice(myLetters) for i in range(12))
    myString2 = ''.join(random.choice(myLetters) for i in range(12))
  elif n == 2:
    myString1 = ''.join(random.choice(myLetters) for i in range(int(list1[1])))
    myString2 = ''.join(random.choice(myLetters) for i in range(int(list1[1])))
  else:
    myString1 = list1[1]
    myString2 = list1[2]
  
  m = len(myString1) 
  n = len(myString2) 
  table = [[None]*(n+1) for i in range(m+1)] 
  for i in range(m+1): 
    for j in range(n+1): 
      if i == 0 or j == 0: 
        table[i][j] = 0
      elif myString1[i-1] == myString2[j-1]: 
        table[i][j] = table[i-1][j-1]+1
      else: 
        table[i][j] = max(table[i-1][j] , table[i][j-1]) 
  
  for a in table:
    print(a)
  print("LCS has length " + str(table[m][n]) )

if __name__ == '__main__':
  inputs = sys.argv
  myLCS_DP(inputs)
