from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        def get_duplicates(nums):
            res = []
            seen = set()

            for n in nums:
                if n in seen:
                    res.append(n)
                seen.add(n)
            
            return res[0]
        
        n = len(nums)

        exp_sum = n * (n + 1) / 2
        som = sum(nums)
        
        duplicated_num = get_duplicates(nums=nums)

        missing_num = int(exp_sum - (som - duplicated_num))

        return [duplicated_num, missing_num]
    

if __name__ == '__main__':

    """ Example 1: """
    nums = [1,2,2,4]
    print(Solution().findErrorNums(nums))