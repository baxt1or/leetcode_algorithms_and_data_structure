class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and (abs(ord(stack[-1]) - ord(c)) == 1 or abs(ord(stack[-1]) - ord(c)) == 25):
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
    


if __name__ == '__main__':
    """ Example 1: """
    s = "zadb"
    print(Solution().resultingString(s))


    """ Example 2: """
    s = "abc"
    print(Solution().resultingString(s))


    """ Example 3: """
    s = "adcb"
    print(Solution().resultingString(s))

    