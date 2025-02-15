class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

      n = self.get_num(num1) + self.get_num(num2)

      result = ''

      while n > 0:
        digit = n % 10
        result = chr(digit+ord('0')) + result
        n //= 10
      
      return result if len(result) != 0 else "0"


    def get_num(self, num):
      
      result = 0

      for c in num:
        digit = ord(c) - ord('0')
        result = result * 10 + digit
      
      return result 
    
if __name__ == '__main__':
  
    """ Example 1: """
    num1 = "456"
    num2 = "77"
    print(Solution().addStrings(num1, num2))


    """ Example 2: """
    num1 = "0"
    num2 = "0"
    print(Solution().addStrings(num1, num2))