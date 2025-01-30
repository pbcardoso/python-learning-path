# The user will input 2 values, which cannot be equal.
# If they are, the user will be alerted. 
# After entering the values, the program will return
# the greater of the two values.

def green(text):
    return f"\033[32m{text}\033[m"
def red(text):
    return f"\033[31m{text}\033[m"

def bigger(first_value, second_value):

    first_value_is_not_numeric = not isinstance(first_value, (float, int, complex))
    second_value_is_not_numeric = not isinstance(second_value, (float, int, complex))

    if first_value_is_not_numeric or second_value_is_not_numeric:
        return 'Os valores digitados não podem ser letras ou qualquer outro tipo de caracteres!'

    if first_value > second_value:
        return first_value

    if first_value == second_value:
        return 'Os valores digitados não podem ser iguais!'

    else:
        return second_value
    
def function_tester(bigger_first_value, bigger_second_value, desidered_result):

  result = bigger(bigger_first_value, bigger_second_value)

  if result == desidered_result:
    print(green('\nTEST OK'))
    print(result)

  else:
    print(red('\nTEST FAIL'))
    print(result)

function_tester(5, 5, 'The values can not be equal!')
function_tester(5, 'a', 'The values can not be letters or any other type of characters!')
function_tester(5, 3, 5)
function_tester(3, 5, 5)
function_tester(3, 3, 'The values can not be equal!')
function_tester('$', 3, 'The values can not be letters or any other type of characters!')
function_tester(-3, 5, 5)
function_tester(-3, -5, -3)
