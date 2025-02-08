import string

class Solution:
    def replaceDigits(self, s: str) -> str:
        
        s = list(s)
        ans = ''

        for i in range(len(s)):
            if s[i].isdigit():
                ans+=self.shift(s[i-1], int(s[i]))
            else:
                ans+=s[i]
        return ans
    
    def shift(self, ch, n):
        letters = list(string.ascii_lowercase)

        for i in range(len(letters)):
            if letters[i] == ch:
                return letters[i+n]
        return -1
    
if __name__ == "__main__":
    s = "a1c1e1"

    print(Solution().replaceDigits(s))