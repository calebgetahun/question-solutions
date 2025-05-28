class Solution:
    def romanToInt(self, s: str) -> int:
        #if no subtractions, add numbers together. If we have a case before a letter, we must take care of said number. All subtractions come in pairs, so pairs should be dealt with as they come. Checks should also come in pairs as we iterate.
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        i = 0
        while i < len(s):
            curr = 0
            if s[i] == "I" and i < len(s) - 1:
                if s[i+1] == "V" or s[i+1] == "X":
                    curr = numerals[s[i+1]] - numerals[s[i]]
                    i += 1
                else:
                    curr = numerals[s[i]]

            elif s[i] == "X" and i < len(s) - 1:
                if s[i+1] == "L" or s[i+1] == "C":
                    curr = numerals[s[i+1]] - numerals[s[i]]
                    i += 1
                else:
                    curr = numerals[s[i]]

            elif s[i] == "C" and i < len(s) - 1:
                if s[i+1] == "D" or s[i+1] == "M":
                    total += numerals[s[i+1]] - numerals[s[i]]
                    i += 1
                else:
                    curr = numerals[s[i]]
                #no subtractions
            else:
                curr = numerals[s[i]]
            total += curr
            i += 1

        return total
    
if __name__ == "__main__":
    sol = Solution()
    test_cases = ["III", "LVIII", "MCMXCIV", "XLIX"]
    expected = [3, 58, 1994, 49]
    for i in range(len(test_cases)):
        print(sol.romanToInt(test_cases[i]) == expected[i])

# TC: O(N), as we check each character in our string with a series of constant time checks
# SC: O(1), as numeral map doesn't depend on size of input