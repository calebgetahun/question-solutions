class Solution:
    def myAtoi(self, s: str) -> int:
        high, low = 2**31 - 1, -2**31
        isPositive = True
        dig = False
        signSeen = False
        arr = []
        
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        while i < len(s):
            if not s[i].isnumeric() and s[i] != "+" and s[i] != "-":
                break
            if s[i] == "+" or s[i] == "-":
                if not dig and not signSeen:
                    isPositive = True if s[i] == "+" else False
                    signSeen = True
                else:
                    break
            if s[i].isnumeric():
                arr.append(s[i])
                dig = True
            i += 1
        
        if not arr:
            return 0
        num = int("".join(arr))
        if not isPositive:
            num *= -1

        if num < 0:
            if num >= low:
                return num
            return low
        elif num > 0:
            if num <= high:
                return num
            return high
        else:
            return 0
    
    def myAtoiWithOverflowCheck(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        isPositive = True
        res = 0

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        if i < len(s) and s[i] == "+":
            isPositive = True
            i += 1
        elif i < len(s) and s[i] == "-":
            isPositive = False
            i += 1
                
        while i < len(s) and s[i].isdigit():
            curr = int(s[i])
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and curr > INT_MAX % 10):
                if isPositive:
                    return INT_MAX
                else:
                    return INT_MIN
            res = (10 * res) + curr
            i += 1

        return res if isPositive else -res

if __name__ == "__main__":
    sol = Solution()
    nums = ["", "   -042", "42", "0-1", "+-10", "035", "yes the number is 340"]
    for num in nums:
        print(sol.myAtoi(num), end=" ")
        print(sol.myAtoiWithOverflowCheck(num))

#TC: O(N)
#SC: O(1) since the most amount of characters we could have will fit into an integer