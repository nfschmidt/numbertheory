
def gcd(number1, number2):
    '''Compute the greatest common divisor of a and b.'''

    _check_not_all_zero((number1, number2))
    lower, greater = sorted((abs(number1), abs(number2)))
    if lower == 0:
        return greater

    return gcd(lower, greater % lower)

def gcd_linear_combination(number1, number2):
    '''Return x, y such that x*a + y*b == gcd(a, b), using euclid's algorithm.'''

    _check_not_all_zero((number1, number2))
    coeficient1, coeficient2 = _gcd_linear_combination_non_negatives(abs(number1), abs(number2))

    if number1 < 0:
        coeficient1 *= -1
    if number2 < 0:
        coeficient2 *= -1

    return coeficient1, coeficient2

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
        
    return x, y

