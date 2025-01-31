from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0 or n == 1:
            return ["()"]

        res = []
        curr = ["("]
        
        def backtrack(curr, open_par, close_par, is_open):
            if len(curr) == (n*2):
                res.append("".join(curr))
                return
            
            if is_open:
                curr.append(")")
                backtrack(curr, open_par, close_par+1, open_par != (close_par+1))
                curr.pop()
            
            if open_par != n:
                curr.append("(")
                backtrack(curr, open_par+1, close_par, (open_par+1) != close_par)
                curr.pop()
            
        backtrack(curr, 1, 0, True)

        return res
    
if __name__ == "__main__":
    sol = Solution()

    for i in range(1, 7):
        paren = sol.generateParenthesis(i)
        print(paren)
        print(len(paren))

# TC: O(4^N / sqrt(N)), based on a few things:
#     - As we have two decisions to make for each decision: closed or open parentheses -> O(2^(N))
#     - But since our recursion depth doesn't just go to N levels, it goes to 2N (as our solutions have to all be 2N in length) -> O(2^(2N)) = O(4^N)
#     - We also perform linear time complexity operations when we are copying our parentheses combinations to our final array
#     - So far, our complexity is O(4^N * N)
#     - Since the validity of each separate path is called into question (aka must be a valid parentheses sequence),
#       the catalan numbers give us an approximation of how these kinds of sequences grow asymptotically, 

#     - The Catalan Numbers grow, Cn ~ (4^N) / (N^(3/2) * sqrt(pi)) as n goes up aka the same n in our problem.
#     - Simply taking this complexity and applying the face that we have a linear O(N) operation at each step, we can ignore the pi term for time
#       complexity purposes and apply our numerator from before to get O((4^N) * N) / (N^(3/2))
#     - This simplifies to O((4^N) / N^(1/2)) or O(4^N / sqrt(N))

# SC: O(N), only including auxilary space (not the space needed for our final solution) as our recursion depth goes 2N levels -> O(N)
