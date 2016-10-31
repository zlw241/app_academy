

def sum_of_squares(n):
    if n <= 1:
        return 1
    else:
        return n**2 + sum_of_squares(n-1)

def square_of_sum(n):
    return (sum(range(1,n+1)))**2


def sum_square_difference(n):
    return square_of_sum(n) - sum_of_squares(n)

print(sum_square_difference(100))