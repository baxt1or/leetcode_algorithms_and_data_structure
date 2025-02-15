from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        occurences = []
        result = []

        
        for i in range(len(nums)):
          if nums[i] == x:
            occurences.append(i)
        
        total = len(occurences)

        for i in range(len(queries)):
          if queries[i] <= total:
            result.append(occurences[queries[i]-1])
          else:
            result.append(-1)
        
        return result


if __name__ == '__main__':

    """ Example 1: """
    nums = [1,3,2,2,3,3,1,3,1]
    queries = [5,6,1,5,6,4,1,5]
    x = 3
    print(Solution().occurrencesOfElement(nums, queries, x))