from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        count = {}
        max_val = -1

        for n in arr:
            count[n] = count.get(n,0)+1
        
        for key, val in count.items():
            if key == val:
                max_val = max(max_val, key)
        return max_val


if __name__ == '__main__':

    """ Example 1: """
    nums = [2,2,2,3,3]
    print(Solution().findLucky(nums))