class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp = ""

        for c in s:
            if c.isalpha() or c.isdigit():
                temp+=c.lower()
        
        l, r = 0, len(temp) - 1

        while l <= r:
            if temp[l] == temp[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True


if __name__ == "__main__":
    """ Example 1: """
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))
