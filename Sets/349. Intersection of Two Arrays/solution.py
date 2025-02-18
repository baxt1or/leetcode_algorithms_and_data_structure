from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums2 = set(nums2)
        
        res = set()

        for num in nums1:
            if num in nums2:
                res.add(num)
        
        return list(res)

if __name__ == '__main__':

    """ Example 1: """
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersection(nums1, nums2))