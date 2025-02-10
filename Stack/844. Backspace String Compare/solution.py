class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.remove_hashtag(s) == self.remove_hashtag(t)
    
    def remove_hashtag(sefl, s):
        stack = []

        for i in range(len(s)):
            if stack and s[i] == "#":
                stack.pop()
            elif s[i] != '#':
                stack.append(s[i])
        return "".join(stack)


if __name__ == "__main__":

    """ Example 1: """
    s = "y#fo##f"
    t = "y#f#o##f"
    print(Solution().backspaceCompare(s, t))