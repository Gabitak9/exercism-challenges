def square_of_sum(number):
    return sum(unit+1 for unit in range(number)) ** 2


def sum_of_squares(number):
    return sum((unit+1) ** 2 for unit in range(number))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
