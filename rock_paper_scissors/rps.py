import sys
print(sys.version)

def rock_paper_scissors(n):
  if n == 0: 
    return [[]]
  elif n == 1: 
     return [['rock'], ['paper'], ['scissors']]   
  return over_two(rock_paper_scissors(n-1))    

def over_two(rps):
  current = []
  standard = [['rock'], ['paper'], ['scissors']]
  for i in rps: 
    for j in standard:
      current.append(i+j)
  return current 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

print(rock_paper_scissors(3))