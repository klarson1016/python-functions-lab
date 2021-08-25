# Challenge 1
def sum_to(n):
  sum = 0
  for x in range(n+1):
    sum += x 
  return(sum) 
print(sum_to(6))


# Chanllenge 2

def largest( list ):
  max = list[0]
  for x in list:
    if x > max:
      max = x
  return max
print(largest([10, 4, 2, 231, 91, 54]))

# Challenge 3 

def occurances(str, sub):
  count = start = 0
  while True:
    start = str.find(sub, start) + 1
    if start > 0:
      count += 1
    else:
      return count
print(occurances('fleep floop', 'e'))


#  Challenge 4
def product(*args):
  result = 1
  for x in args:
    result *= x
  return result
print(product(-1, 4))