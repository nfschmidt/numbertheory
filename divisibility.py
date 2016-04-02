
def gcd(a, b):
    '''Compute the greatest common divisor of a and b'''

    lower, greater = sorted((abs(a), abs(b)))
    if lower == 0:
        if greater != 0:
            return greater
        else:
            raise ValueError('Both numbers cannot be 0')
    
    return gcd(lower, greater % lower)
