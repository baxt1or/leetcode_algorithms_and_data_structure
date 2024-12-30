from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """ Returns the count of 1's in their binary representation """
        bins =  [bin(i) for i in range(n+1)]
        
        ans = []
        for x in bins:
            if x.count('1') >= 1:
                ans.append(x.count('1'))
            else:
                ans.append(0)
        return ans

""" Example 1: """
n = 2
Solution().countBits(n)

""" Example 2: """
n = 5
Solution().countBits(n)