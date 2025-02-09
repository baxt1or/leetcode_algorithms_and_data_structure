from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0)+1
        
        freq = sorted(freq.items() , key=lambda item:item[0] , reverse=True)

        freq = dict(freq)

        new_freq = sorted(freq.items(), key=lambda item:item[1])

        res = []

        for key, val in dict(new_freq).items():
            res.extend([key]*val)
        
        return res
    

if __name__ == "__main__":
   
   nums = [2,3,1,3,2]

   """ Output: [1,3,3,2,2]
   Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order. """ 
   print(Solution().frequencySort(nums))