class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if stack and s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
    
if __name__ == "__main__":
    """ Example 1: """
    s = "leet**cod*e"
    print(Solution().removeStars(s))

    """ Example 2: """
    s = "erase*****"
    print(Solution().removeStars(s))