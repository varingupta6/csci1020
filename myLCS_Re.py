import sys
import random

def recursion(X, Y, m, n):
  if m == 0 or n == 0: 
    return 0
  elif X[m-1] == Y[n-1]: 
    return 1 + recursion(X, Y, m-1, n-1); 
  else: 
    return max(recursion(X, Y, m, n-1), recursion(X, Y, m-1, n)); 

def myLCS_Re(list1):
  n = len(list1)
  myLetters = ["A", "T", "C", "G"]
  if n == 1:
    myString1 = ''.join(random.choice(myLetters) for i in range(12))
    myString2 = ''.join(random.choice(myLetters) for i in range(12))
  elif n == 2:
    myString1 = ''.join(random.choice(myLetters) for i in range(int(list1[1])))
    myString2 = ''.join(random.choice(myLetters) for i in range(int(list1[1])))
  else:
    myString1 = list1[1]
    myString2 = list1[2]

  print ("LCS has length " + str(recursion(myString1 , myString2, len(myString1), len(myString2))))


if __name__ == '__main__':
  inputs = sys.argv
  myLCS_Re(inputs)
