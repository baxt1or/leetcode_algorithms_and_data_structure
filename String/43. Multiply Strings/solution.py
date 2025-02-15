class Solution:
    def multiply(self, num1: str, num2: str) -> str:

      return str(self.get_digit(num1) * self.get_digit(num2))
    
    def get_digit(self, num):

      result = 0

      for c in num:
        digit = ord(c) - ord('0')
        result = result * 10 + digit
      
      return result


if __name__ == '__main__':
   
   """ Example 1: """
   num1 = "2"
   num2 = "3"
   print(Solution().multiply(num1, num2))

   """ Example 2: """
   num1 = "123"
   num2 = "456"
   print(Solution().multiply(num1, num2))