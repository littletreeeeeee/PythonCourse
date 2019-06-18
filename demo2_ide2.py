def get_digit(x):
    """

    :type x: int or float
    """
    returnDigit = 0
    while x > 0:
        returnDigit += 1
        x /= 10
    return returnDigit


print "12345 has digit:", get_digit(10)
print "2^512 has digit:", get_digit(2**512)
print "12345 has digit:", get_digit("12345")
