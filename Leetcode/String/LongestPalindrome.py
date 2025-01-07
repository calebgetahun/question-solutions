class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count the occurence of each character and the number of characters with even counts + one extra character can be used
        chars = dict()
        for char in s:
            indx = ord(char) - ord('A')
            chars[indx] = chars.get(indx, 0) + 1
        
        letters = 0
        one_odd = True

        for i in chars.values():
            if i % 2 == 0:
                letters += i

            else:
                letters += ((i // 2) * 2)
                if one_odd:
                    letters += 1
                    one_odd = False
    
        return letters

if __name__ == "__main__":
    sol = Solution()
    str_case = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    print(sol.longestPalindrome(str_case))

# TC: O(N)
# SC: O(1) since all characters are either uppercase or lower case English letters