#!/usr/bin/python
import math
import argparse

def find_max_profit(prices):
  # Give me another list of the same numbers sorted least to greatest
  for i in range(len(prices)):
    if prices.index(min(prices)) < prices.index(max(prices)):
      return max(prices) - min(prices)
    elif prices.index(max(prices)) == 0 and prices.index(min(prices)) == len(prices) - 1:
      diff = [prices[i+1]-prices[i] for i in range(len(prices)-1)] 
      return max(diff)
    elif prices.index(min(prices)) == len(prices) - 1:
      prices.remove(min(prices))
      find_max_profit(prices)
    elif prices.index(max(prices)) == 0:
      prices.remove(max(prices))
      find_max_profit(prices)
    

  
# x = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]
# y = [1, 55, 678, 3, 3214]
# z = [1050, 270, 1540, 3800, 2]
# v = [100, 90, 80, 50, 20, 10]
# print(find_max_profit(v))
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
