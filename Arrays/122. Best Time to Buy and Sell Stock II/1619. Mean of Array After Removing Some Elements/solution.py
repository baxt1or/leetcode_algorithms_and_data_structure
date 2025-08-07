from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        arr.sort()

        smallest = int(len(arr) * 0.05)
        largest = int(len(arr) - smallest)

        nums = arr[smallest:largest]

        return sum(nums) / len(nums)
    

if __name__ == '__main__':
    """ Example 1: """

    arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
    print(Solution().trimMean(arr=arr))


    """ Example 2: """
    arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
    print(Solution().trimMean(arr=arr))