def are_string_equal(s1, s2):
    for i in range(len(s1)):
        if s1[i].lower() == s2[i].lower():
            continue
        
        if ord(s1[i].lower()) < ord(s2[i].lower()):
            return -1

        if ord(s2[i].lower()) < ord(s1[i].lower()):
            return 1

    return 0

if __name__ == "__main__":
    string_one = input()
    string_two = input()

    print(are_string_equal(string_one, string_two))