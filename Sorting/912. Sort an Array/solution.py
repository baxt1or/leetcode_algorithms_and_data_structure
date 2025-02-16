from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        if n <= 1:
            return nums
        
        mid = n //2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, left, right):

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

if __name__ == "__main__":

    """ Example 1: """
    nums = [5,1,1,2,0,0]
    print(Solution().sortArray(nums))