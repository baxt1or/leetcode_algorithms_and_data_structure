from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        count = {}

        for i in range(len(nums)):
            key = nums[i] - i
            count[key] = count.get(key, 0) +1

        for key, val in count.items():
            count[key] = val * (val - 1)  / 2
        
        n = len(nums)

        total = n * (n-1) /2

        total_good_pairs = sum(count.values())

        return int(total - total_good_pairs)


if __name__ == "__main__":
    nums = [4,1,3,3]
    """ Output: 5
    Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
    The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
    The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
    The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
    The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
    There are a total of 5 bad pairs, so we return 5. """
    
    print(Solution().countBadPairs(nums))