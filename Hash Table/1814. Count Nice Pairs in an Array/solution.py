from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        count = {}

        for i in range(len(nums)):
            key = nums[i] - self.rev(nums[i])
            count[key] = count.get(key, 0)+1
        
        result = 0
        for val in count.values():
            result = (result + (val * (val -1) /2)) % MOD

        return int(result)
            
    
    def rev(self,n):
        return int("".join(list(reversed(str(n)))))


if __name__ == "__main__":
    nums = [42,11,1,97]
    
    """ Output: 2
    Explanation: The two pairs are:
    - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
    - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12. """ 

    print(Solution().countNicePairs(nums))