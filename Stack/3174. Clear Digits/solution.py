class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == "__main__":
    
    """ Example 1: """
    s = 'abc'
    print(Solution().clearDigits(s))

    """ Example 2: """
    s = 'cb34'
    print(Solution().clearDigits(s))