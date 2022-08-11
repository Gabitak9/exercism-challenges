def steps(number):

    if number < 1 or number != int(number):
        raise ValueError("Only positive integers are allowed")
    
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = number * 3 + 1
        steps += 1
    
    return steps
