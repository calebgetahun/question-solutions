if __name__ == "__main__":
    first, second = 1, 2
    even_sum = 0

    while second < 4000000:
        if second % 2 == 0:
            even_sum += second
        
        temp = first
        first = second
        second += temp

    print(even_sum)

