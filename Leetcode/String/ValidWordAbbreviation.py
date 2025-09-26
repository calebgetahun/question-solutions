class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #set pointers for words
        c_in = a_in = 0

        #check while both indices are valid
        while a_in < len(abbr) and c_in < len(word):
            #if abbr is a letter
            if abbr[a_in].isalpha():
                if abbr[a_in] != word[c_in]:
                    return False
                c_in += 1
                a_in += 1
            #if abbr char is a number
            else:
                #leading 0 check
                if abbr[a_in] == "0":
                    return False
                
                #create array to concatenate numbers together for checking
                temp = []
                while a_in < len(abbr) and abbr[a_in].isnumeric():
                    temp.append(abbr[a_in])
                    a_in += 1

                #integer conversion
                num_letters = int("".join(temp))
                c_in += num_letters
            
        return c_in == len(word) and a_in == len(abbr)
                
if __name__ == "__main__":
    sol = Solution()
    word = "substitution"
    abbreviations = ["s10n", "sub4u4", "12", "s55n", "s010n"]
    for a in abbreviations:
        print(sol.validWordAbbreviation(word, a))

# TC: O(N + M)
# SC: O(1)