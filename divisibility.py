
def gcd(number1, number2):
    '''Compute the greatest common divisor of n1 and n2.'''

    result, _, _ = gcd_linear_combination(number1, number2)
    return result

def gcd_linear_combination(number1, number2):
    '''Return g, x, y such that x*n1 + y*n2 == g and g == gcd(n1, n2).'''

    _check_not_all_zero((number1, number2))
    abs_n1, abs_n2 = abs(number1), abs(number2)

    gcd, coeficient1, coeficient2 = _gcd_linear_combination_non_negatives(abs_n1, abs_n2)
    if number1 < 0:
        coeficient1 *= -1
    if number2 < 0:
        coeficient2 *= -1

    return gcd, coeficient1, coeficient2

def _check_not_all_zero(numbers):
    if not [n for n in numbers if n != 0]:
        raise ValueError('All numbers cannot be 0')

def _gcd_linear_combination_non_negatives(number1, number2):
    x, next_x = 1, 0
    y, next_y = 0, 1
    reminder, next_reminder = number1, number2

    while next_reminder:
        quotient = reminder // next_reminder
        x, next_x = next_x, x - quotient * next_x
        y, next_y = next_y, y - quotient * next_y
        reminder, next_reminder = next_reminder, reminder - quotient * next_reminder

    return reminder, x, y
