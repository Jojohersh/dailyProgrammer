#!/usr/bin/python

import sys

def checkOrder(word):
  i = 0
  wordLen = len(word)
  isInOrder = True
  isInReverseOrder = True
  #check through word to see if it is in regular order
  for i in range(0, wordLen-2):
    if (word[i] > word[i+1]):
      #if the letters aren't in order, break
      isInOrder = False
      break
  #check through word to see if it is in reverse order
  for i in range(0, wordLen-2):
    if (word[i] < word[i+1]):
      #if the letters aren't in reverse order, break
      isInReverseOrder = False
      break
  #determine what to return
  if (isInOrder):
    return "IN ORDER"
  elif (isInReverseOrder):
    return "IN REVERSE ORDER"
  else:
    return "NOT IN ORDER"


if __name__ == "__main__":
  #file name hardcoded...
  f = open('words.txt', 'r')
  for line in f:
    line = line.strip()
    print line," ",checkOrder(line)
