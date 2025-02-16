from typing import List

class Algorithm:

    def selectionSort(self, nums:List[int]) -> None:
        
        n:int = len(nums)

        for i in range(n):
            min_index : int = i
            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j 
            nums[i], nums[min_index] = nums[min_index], nums[i]
        

if __name__ == '__main__':

    """ Example 1: """
    nums = [7, 4,23,1,5,6]
    Algorithm().selectionSort(nums)
    print(nums)
