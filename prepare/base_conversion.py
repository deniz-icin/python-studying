def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')
    if not all(0 <= d < input_base for d in digits):
        raise ValueError('all digits must satisfy 0 <= d < input base')

""" if any(d >= input_base for d in digits): 
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if any(d < 0 for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
"""

        
    number = 0
    for d in digits:
        number = number * input_base + d

    # number = sum(d*input_base**i for i,d in enumerate(digits[::-1]))
    
    if number == 0: 
        return [0]
    
    out_digits = []
    while number != 0:
        number, digit = divmod(number, output_base)
        out_digits.insert(0, digit)

        return out_digits

"""    new_digits.insert(0, number%output_base)
       number = number//output_base
"""
    