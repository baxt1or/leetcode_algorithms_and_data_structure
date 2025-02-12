from typing import List
import math

class Solution:
    def is_prime(self, n: int) -> bool:
        """ Optimized prime check using O(√N) complexity """
        if n < 2:
            return False
        if n == 2: 
            return True
        if n % 2 == 0: 
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        n = len(nums)
        
        main = []

        for i in range(n):
          num = nums[i][i]
          
          if self.is_prime(num):
            main.append(num)
        
        for i in range(n):
            num = nums[i][n-1-i]
            if self.is_prime(num):
              main.append(num)
        
        return max(main) if main else 0

if __name__ == '__main__':

    """ Example 1: """
    nums =[[1,2,3],[5,6,7],[9,10,11]]
    print(Solution().diagonalPrime(nums=nums))

    """ Example 2: """
    nums = [[1,2,3],[5,17,7],[9,11,10]]
    print(Solution().diagonalPrime(nums=nums))