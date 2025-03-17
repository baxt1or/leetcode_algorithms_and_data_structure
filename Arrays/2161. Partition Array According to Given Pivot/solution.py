from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        

        start = []
        middle = []
        ends = []

        for x in nums:
            if x < pivot:
                start.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                ends.append(x)
            

        return start+middle+ends
    


if __name__ == '__main__':

    """ Example 1: """
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    print(Solution().pivotArray(nums, pivot))