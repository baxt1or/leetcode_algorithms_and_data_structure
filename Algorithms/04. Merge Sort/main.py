from typing import List

class Algorithm:
    def mergeSort(self, nums:List[int]) -> List[int]:

        n: int = len(nums)

        if n <= 1:
            return nums
        
        mid :int = n // 2

        left : List[int] = self.mergeSort(nums[:mid])
        right : List[int] = self.mergeSort(nums[mid:])

        return self.merge(left=left, right=right)
    
    def merge(self,left:List[int], right:List[int]) -> List[int]:

        merged : List[int] = []
        i : int = 0
        j:int = 0

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


if __name__ == '__main__':
    """ Example 1: """
    nums = [9,0,5,24,6,32,12,5,57,1,2]
    print(Algorithm().mergeSort(nums=nums))