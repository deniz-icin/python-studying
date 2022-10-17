def steps(number):
    result = 0
    if number == 1:
        return result
    if number <= 0:
      raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            result += 1
        else:
            number = number*3 + 1
            result += 1
    return result

steps()