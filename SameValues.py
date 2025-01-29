# A program that reads two values and prints the largest one, not allowing the values to be equal.

firstValue = int(input('First value: '))
secondValue = int(input('\nSecond value: '))

if firstValue == secondValue:
  print('\nThe two values entered are the same!')

elif secondValue > firstValue:
  print('\nThe higher value is: \033[31m{}\033[m'.format(secondValue))

else:
  print('\nThe higher value is: \033[31m{}\033[m'.format(firstValue))
