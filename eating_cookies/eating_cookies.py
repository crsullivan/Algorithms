#!/usr/bin/python
# Getting started
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  n_factorial = 1
  nr_factorial = 1
  for i in range(1, n+1):
    n_factorial = n_factorial * i

  for j in range(1, n):
    nr_factorial = nr_factorial * j

  perm = n_factorial 

  return perm
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')