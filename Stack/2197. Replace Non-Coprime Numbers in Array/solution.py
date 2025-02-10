import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        stack = []
        i = 0
        for n in nums:
            stack.append(n)
            while len(stack) > 1 and math.gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                r = (a * b) // math.gcd(a , b)
                stack.append(r)
                i+=1
        return stack