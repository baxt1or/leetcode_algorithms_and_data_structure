
class Solution:
    def isValid(self, s: str) -> bool:

        brakets = {"}": "{", "]":"[", ")":"("}

        stack = []

        for c in s:
            if c in brakets.values():
                stack.append(c)
            elif c in brakets.keys():
                if not stack or stack.pop() != brakets[c]:
                    return False
        
        return len(stack) == 0
    



if __name__ == '__main__':

    """ Example 1: """
    s = "()[]{}"
    print(Solution().isValid(s))