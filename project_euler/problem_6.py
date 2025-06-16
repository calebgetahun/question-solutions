def calculate_difference(upper_value):
    sum_of_squares = ((upper_value**2 + upper_value) * (2*upper_value + 1)) // 6
    square_of_sums = ((upper_value * (upper_value + 1)) / 2) ** 2

    return square_of_sums - sum_of_squares

if __name__ == "__main__":
    print(calculate_difference(100))