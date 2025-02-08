import string
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        shifts = self.cum_sum(shifts)
        ans = ''

        for i in range(len(s)):
            ans+=self.shift(s[i], shifts[i])
        return ans

    
    def shift(self, c, n):
    
        letters = list(string.ascii_lowercase)

        for i in range(len(letters)):
            if letters[i] == c:
                new_idx = (i+n) % 26
                return letters[new_idx]
        return -1
    
    def cum_sum(self, shifts):
        shifts = list(reversed(shifts))

        som = 0
        res = []
        for i in range(len(shifts)):
            som+=shifts[i]
            res.append(som)
        return list(reversed(res))


if __name__ == "__main__":
    s = "abc"
    shifts = [3,5,9]

    print(Solution().shiftingLetters(s, shifts))