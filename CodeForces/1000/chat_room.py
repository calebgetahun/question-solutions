def is_hello(s):
    if len(s) < 5:
        return "NO"
    
    curr = 0
    hello = "hello"
    curr_hello = 0
    while curr < len(s):
        if s[curr] == hello[curr_hello]:
            curr_hello += 1
            if curr_hello == 5:
                return "YES"
        curr += 1

    return "NO"

if __name__ == "__main__":
    hello = input()
    print(is_hello(hello))