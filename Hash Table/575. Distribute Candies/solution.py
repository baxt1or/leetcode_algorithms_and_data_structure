from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        nums_allowed = len(candyType) / 2
        
        unique_type = len(set(candyType))
       
        return int(min(nums_allowed, unique_type))


if __name__ == '__main__':
    """ Example 1:  """
    candyType = [1,1,2,2,3,3]
    print(Solution().distributeCandies(candyType))

    """ Example 2: """
    candyType = [6,6,6,6]
    print(Solution().distributeCandies(candyType))
