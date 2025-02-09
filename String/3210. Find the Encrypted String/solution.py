class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = ''
        
        for i in range(len(s)):
          index = (i + k) % len(s)
          ans+=s[index]
        return ans
    
if __name__ == "__main__":
   s = "dart"
   k = 3

   """Explanation:

   For i = 0, the 3rd character after 'd' is 't'.
   For i = 1, the 3rd character after 'a' is 'd'.
   For i = 2, the 3rd character after 'r' is 'a'.
   For i = 3, the 3rd character after 't' is 'r'."""

   print(Solution().getEncryptedString(s,k))