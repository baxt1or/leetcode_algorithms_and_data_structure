from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        n = self.get_num("".join([str(x) for x in num])) + k

        return [self.get_num(c) for c in self.get_str(n)]
    
    def get_num(self, num):

      result = 0

      for c in num:
        
        digit = ord(c) - ord('0')
        result = result * 10 + digit

      return result
    
    def get_str(self, n):

      result = ''

      while n > 0:
        
        digit = n % 10
        result = chr(digit+ord('0')) + result
        n //= 10
      
      return result if len(result) != 0 else '0'


if __name__ == '__main__':
    
    """ Example 1: """
    num = [1,2,0,0]
    k = 34
    print(Solution().addToArrayForm(num, k))


    """ Example 2: """
    num = [2,1,5]
    k = 806
    print(Solution().addToArrayForm(num, k))