from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        

        nums = sorted(list(set(arr)))
        
        ranks = {}

        for i in range(len(nums)):
          ranks[nums[i]] = i+1
        
        res = []

        for n in arr:
          res.append(ranks[n])
        
        return res

if __name__ == '__main__':
    
    """ Example 1: """
    arr = [37,12,28,9,100,56,80,5,12]
    print(Solution().arrayRankTransform(arr=arr))


    """ Example 2: """
    arr = [100,100,100]
    print(Solution().arrayRankTransform(arr=arr))