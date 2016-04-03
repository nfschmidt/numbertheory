
def gcd(a, b):
    '''Compute the greatest common divisor of a and b.'''

    lower, greater = sorted((abs(a), abs(b)))
    if lower == 0:
        if greater != 0:
            return greater
        else:
            raise ValueError('Both numbers cannot be 0')
    
    return gcd(lower, greater % lower)

def gcd_linear_combination(a, b):
    '''Return x, y such that x*a + y*b == gcd(a, b), using euclides' algorithm.'''
    x, y = _gcd_linear_combination_non_negatives(abs(a), abs(b))

    if a < 0: x = -x
    if b < 0: y = -y

    return x, y

def _gcd_linear_combination_non_negatives(n1, n2):
    first_reminder = n1 % n2
    if first_reminder == 0:
        return 0, 1

    quotient = n1 // n2
    first_x = 1
    first_y = -quotient
    
    second_reminder = n2 % first_reminder

    if second_reminder == 0:
        return first_x, first_y

    quotient = n2 // first_reminder
    second_x = -first_x * quotient
    second_y = 1 - first_y * quotient
    
    return _gdc_linear_combination_iteration_result(
        previous_reminder=first_reminder, reminder=second_reminder,
        previous_x=first_x, x=second_x,
        previous_y=first_y, y=second_y
    )

def _gdc_linear_combination_iteration_result(previous_reminder, reminder,
                                             previous_x, x,
                                             previous_y, y):
    quotient = previous_reminder // reminder
    reminder, previous_reminder = (previous_reminder % reminder), reminder
    while reminder:
        x, previous_x = (previous_x - x * quotient), x
        y, previous_y = (previous_y - y * quotient), y

        quotient = previous_reminder // reminder
        reminder, previous_reminder = (previous_reminder % reminder), reminder

    return x, y
