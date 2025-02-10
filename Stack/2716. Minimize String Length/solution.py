class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        stack = []

        for c in s:
            if c not in stack:
                stack.append(c)
        return len(stack)


if __name__ == "__main__":
    """ Example 1: """
    s = "aaabc"
    print(Solution().minimizedStringLength(s))