from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        res = []

        for i in range(len(arr1)):
            count = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) > d:
                    count+=1
                    res.append(count) 
        
        return res.count(len(arr2))