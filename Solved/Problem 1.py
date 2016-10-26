def multiples_sum(number1, number2, max):
  '''
  This function will find the sum of all the natural numbers below parameter "max"
  that are multiples of number1 or number2
  '''
  return sum([x for x in range(max) if x % number1 == 0 or x % number2 == 0])
