class Solution:
    def numberCount(self, a: int, b: int) -> int:
        """ Returns count of Unique Digits """
        result = []
        
        nums = [str(x) for x in range(a, b+1)]

        for s in nums:
            if "".join(dict.fromkeys(s)) == s:
                result.append(s)                
        return len(result)
    

""" Example 1: """
a = 1
b = 20
Solution().numberCount(a, b)

""" Example 2: """
a = 9
b = 19
Solution().numberCount(a, b)

""" Example 3: """
a = 80
b = 120
Solution().numberCount(a, b)