def luhn(num):
    '''The Luhn algorithm checksum formula used to validate id numbers'''
    num = list(map(int, str(num)))
    sum_digits = lambda num: sum(map(int, str(num)))

    odd_digits = list(map(lambda x: sum_digits(x * 2), num[-1::-2]))
    even_digits = num[-2::-2]

    check_digit = (sum(odd_digits) + sum(even_digits)) % 10
    return check_digit
