


def power_digit_sum(digit, power):
    exponentiated = digit**power
    digit_sum = sum([int(i) for i in list(str(exponentiated))]) 
    return digit_sum


print(power_digit_sum(2,1000))