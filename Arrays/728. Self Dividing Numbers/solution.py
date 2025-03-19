from typing import List, defaultdict

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        res = defaultdict(list)
        
        for n in range(left, right+1):
            for x in str(n):
               if int(x) !=0 and n % int(x) == 0:
                   res[str(n)].append(int(x))
        
        nums = []

        for key,val in dict(res).items():
            if len(key) == len(val):
                nums.append(int(key))
        
        return nums


if __name__ == '__main__':

    """ Example 1: """
    left = 1
    right = 22
    print(Solution().selfDividingNumbers(left, right))