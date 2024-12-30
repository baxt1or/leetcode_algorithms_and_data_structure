class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """ Returns True if n is divisible by 3 """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0 and self.isPowerOfThree(n//3):
            return True
        else:
            return False

""" Example 1: """
n = 27
Solution().isPowerOfThree(n)

""" Example 2: """
n = 0
Solution().isPowerOfThree(n)

""" Example 3: """
n = -1
Solution().isPowerOfThree(n)

""" Example 4: """
n = 9
Solution().isPowerOfThree(n)