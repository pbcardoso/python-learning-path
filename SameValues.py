# A program that reads two values and prints the largest one, not allowing the values to be equal.

first_value = int(input('First value: '))
second_value = int(input('\nSecond value: '))

if first_value == second_value:
  print('\nThe two values entered are the same!')

elif second_value > first_value:
  print('\nThe higher value is: \033[31m{}\033[m'.format(second_value))

else:
  print('\nThe higher value is: \033[31m{}\033[m'.format(first_value))
