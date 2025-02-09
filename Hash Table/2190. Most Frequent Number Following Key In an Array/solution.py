from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:

        count = {}

        for i in range(len(nums)-1):
            if nums[i] == key:
                val = nums[i+1]
                count[val] = count.get(val , 0) + 1
        return max(count, key=count.get)


if __name__ == "__main__":

    nums = [1,100,200,1,100]
    key = 1

    """ Output: 100
        Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
        No other integers follow an occurrence of key, so we return 100. """

    print(Solution().mostFrequent(nums, key))