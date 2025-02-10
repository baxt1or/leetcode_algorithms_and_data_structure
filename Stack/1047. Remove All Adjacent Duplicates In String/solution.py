class Solution:
    def removeDuplicates(self, s: str) -> str:
      stack = []
      
      
      for i in range(len(s)):
        if stack and stack[-1] == s[i]:
          stack.pop()
        else:
          stack.append(s[i])
      return "".join(stack)


if __name__ == "__main__":
  
  """ Example 1: """
  s = 'abbaca'
  print(Solution().removeDuplicates(s))
  
  s = "azxxzy"
  """ Example 2: """
  print(Solution().removeDuplicates(s))