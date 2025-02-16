from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
        res = set()
        xor = 0
        count={}

        for n in nums:
            count[n] = count.get(n, 0)+1
        
        for key, val in count.items():
            if val == 2:
                xor ^=key
        
        return xor
            

if __name__ == '__main__':

    """ Example 1: """
    nums = [1,2,2,1]
    print(Solution().duplicateNumbersXOR(nums))