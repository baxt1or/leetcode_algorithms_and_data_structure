from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = "".join([chr(x + ord('0')) for x in digits])

        res = self.int_to_str(self.str_to_int(num)+1)

        return [self.str_to_int(c) for c in res]
    
    def int_to_str(self, n):
      
      result = ''

      while n >0 :
        digit = n % 10
        result = chr(digit + ord('0')) + result
        n//=10
      return result
    
    def str_to_int(self, s):

      result = 0

      for c in s:
        digit = ord(c) - ord('0')
        result = result*10+digit

      return result
    

if __name__ == '__main__':
    
    """ Example 1: """
    digits = [1,2,3]
    print(Solution().plusOne(digits=digits))