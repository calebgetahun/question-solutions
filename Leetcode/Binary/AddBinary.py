class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary = []

        a_pos, b_pos = len(a) - 1, len(b) - 1
        rem = 0
        
        while a_pos >= 0 or b_pos >= 0:
            temp = 0
            if a_pos > -1:
                if a[a_pos] == "1":
                    temp += 1
            if b_pos > -1:
                if b[b_pos] == "1":
                    temp += 1
            if rem:
                temp += 1
            
            match temp:
                case 0:
                    binary.append("0")
                case 1:
                    binary.append("1")
                    rem = 0
                case 2:
                    binary.append("0")
                    rem = 1
                case 3:
                    binary.append("1")
                    rem = 1
                
            
            a_pos -= 1
            b_pos -= 1

        if rem:
            binary.append("1")
        
        return "".join(binary[::-1])

if __name__ == "__main__":
    sol = Solution()
    a, b = "101001", "1101"
    print(sol.addBinary(a, b))

# TC: O(N), where N is the max between a and b
# SC: O(N), where N is the max between a and b