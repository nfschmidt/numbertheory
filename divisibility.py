
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
    first_reminder = number1 % number2
    if first_reminder == 0:
        return 0, 1

    quotient = number1 // number2
    first_x = 1
    first_y = -quotient

    second_reminder = number2 % first_reminder

    if second_reminder == 0:
        return first_x, first_y

    quotient = number2 // first_reminder
    second_x = -first_x * quotient
    second_y = 1 - first_y * quotient

    return _gcd_linear_combination_iteration_result(
        previous_reminder=first_reminder, reminder=second_reminder,
        previous_x=first_x, current_x=second_x,
        previous_y=first_y, current_y=second_y
    )

def _gcd_linear_combination_iteration_result(previous_reminder, reminder,
                                             previous_x, current_x,
                                             previous_y, current_y):
    quotient = previous_reminder // reminder
    reminder, previous_reminder = (previous_reminder % reminder), reminder
    while reminder:
        current_x, previous_x = (previous_x - current_x * quotient), current_x
        current_y, previous_y = (previous_y - current_y * quotient), current_y

        quotient = previous_reminder // reminder
        reminder, previous_reminder = (previous_reminder % reminder), reminder

    return current_x, current_y
