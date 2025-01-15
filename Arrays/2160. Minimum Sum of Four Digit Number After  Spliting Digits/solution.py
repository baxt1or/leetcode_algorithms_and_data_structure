class Solution:
    def minimumSum(self, num: int) -> int:
        """ Returns the Minimum Sum of Four Digits """
        
        res = [int(x) for x in str(num)]
        
        ans = [] 
        
        while len(res) != 0:
            min_val = min(res)
            max_val = max(res)
            ans.append(min_val)
            ans.append(max_val)
            res.remove(min_val)
            res.remove(max_val)
        
        return int("".join(map(str, ans[:2]))) + int("".join(map(str, ans[2:])))
     
""" Example 1: """            
num = 5592
Solution().minimumSum(num)

""" Example 2: """
num = 2932
Solution().minimumSum(num)

""" Example 3: """
num = 4009
Solution().minimumSum(num)