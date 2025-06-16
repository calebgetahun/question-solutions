def sum_of_multiples(multiple_one, multiple_two, upper_range):
    first = (upper_range - 1) // multiple_one #number of multiples of 3 below 1000
    second = (upper_range - 1) // multiple_two #number of multiples of 5 below 1000
    intersections = upper_range // (multiple_one * multiple_two)

    first_sum = (first * (first + 1) / 2) * multiple_one
    second_sum = (second * (second + 1) / 2) * multiple_two
    intersections_sum = (intersections * (intersections + 1) / 2) * (multiple_one * multiple_two)

    return first_sum + second_sum - intersections_sum

if __name__ == "__main__":
    print(sum_of_multiples(3, 5, 1000))