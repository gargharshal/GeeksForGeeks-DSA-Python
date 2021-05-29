get_ipython().run_cell_magic("time", " ", """# Sum of n natural number

# Solution 1
def sum_n_natural_numbers_1(n):
  # order of growth - constant
  return (n*(n+1)/2)

print(sum_n_natural_numbers(5))""")


get_ipython().run_cell_magic("time", "", """def sum_n_natural_numbers_2(n):
  sum = 0
  for i in range(1, n+1): 
    \"\"\"
    there is no point to keep the first 
    value 0 as it will 
    unnecesarrily ran the loop one time extra 
    \"\"\"
    sum += i
  return sum

print(sum_n_natural_numbers_2(5))   """)


get_ipython().run_cell_magic("time", "", """def sum_n_natural_numbers_3(n):
  sum = 0
  for i in range(1, n+1): 
    for j in range(1, i+1):
      sum += 1
  return sum

print(sum_n_natural_numbers_3(5))   """)


def getSum(l): #takes the list
  sum = 0
  for x in l:
    sum += x
  return sum


def getSumodd(l): #return sum of list if odd elements
  if len(l)get_ipython().run_line_magic("2", " == 0:")
    return 0
  sum = 0
  for x in l:
    sum += x
  return sum



