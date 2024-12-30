
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """ Return True if n is divible by 2 and its binary contains only 1 once  """
        return n > 0 and bin(n).count('1') == 1
    

""" Example 1: """
n = 1
Solution().isPowerOfTwo(n)

""" Example 2: """
n = 16
Solution().isPowerOfTwo(n)

""" Example 3: """
n = 3
Solution().isPowerOfTwo(n)