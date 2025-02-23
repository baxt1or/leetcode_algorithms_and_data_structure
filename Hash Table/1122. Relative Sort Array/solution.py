from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        count1 = Counter(arr1)
    
        count = {}

        for i in range(len(arr2)):
            count[arr2[i]] = i 

        res = []

        for key, val in count.items():
            if key in count1:
                res.extend([key]*count1[key])
        
        
        res2 = sorted([x for x in arr1 if x not in set(arr2)])

        return res + res2
        
        
if __name__ == '__main__':

    """ Example 1: """ 
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    print(Solution().relativeSortArray(arr1, arr2))