#!/usr/bin/python

import argparse

def find_max_profit(prices):
  curr_buy = float('inf')
  curr_sell = float('-inf')
  for i in range(len(prices)):
    if prices[i] < curr_buy:
      curr_buy = prices[i]
      print('min', curr_buy)
    for j in range(i + 1, len(prices)):
      profit = prices[j] - prices[i]
      print('j', prices[j])
      print('i', prices[i])
      if profit > curr_sell:
        curr_sell = profit
        print('max', curr_sell)
  return curr_sell

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  printfind_max_profit([1050, 270, 1540, 3800, 2])