def is_armstrong_number(number):

    number_of_digits = len(str(number))

    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit) ** number_of_digits

    if sum_of_digits == number:
        return True
    else:
        return False
