class Solution:
    def hammingWeight(self, n: int) -> int:
        """ Returns total count of 1 in binary representation of n """
        count = 0
        binary_n = bin(n)

        for s in binary_n:
            if s == '1':
                count+=1
        return count



""" Example 1: """
n = 11
Solution().hammingWeight(n)

""" Example 2: """
n = 128
Solution().hammingWeight(n)

""" Example 3:  """
n = 2147483645
Solution().hammingWeight(n)