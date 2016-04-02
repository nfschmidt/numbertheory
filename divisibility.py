
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
        reminder_2=first_reminder, reminder_1=second_reminder,
        x_2=first_x, x_1=second_x,
        y_2=first_y, y_1=second_y
    )

def _gdc_linear_combination_iteration_result(reminder_2, reminder_1,
                                             x_2, x_1, y_2, y_1):
    quotient = reminder_2 // reminder_1
    reminder_1, reminder_2 = (reminder_2 % reminder_1), reminder_1
    while reminder_1:
        x_1, x_2 = (x_2 - x_1 * quotient), x_1
        y_1, y_2 = (y_2 - y_1 * quotient), y_1

        quotient = reminder_2 // reminder_1
        reminder_1, reminder_2 = (reminder_2 % reminder_1), reminder_1

    return x_1, y_1
    
