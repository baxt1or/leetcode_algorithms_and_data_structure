from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l, r = 0, len(s)-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1



if __name__ == '__main__':

    """ Example 1: """
    s = ["h","e","l","l","o"]
    Solution().reverseString(s)
    print(s)


    """ Example 2: """
    s = ["H","a","n","n","a","h"]
    Solution().reverseString(s)
    print(s)