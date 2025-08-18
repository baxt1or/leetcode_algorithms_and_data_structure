class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        max_vowel = 0
        max_cons = 0

        for c, f in count.items():
            if c in vowels:
                max_vowel = max(max_vowel, f)
            else:
                max_cons = max(max_cons, f)
        
        return max_vowel + max_cons


if __name__ == '__main__':
    """ Example 1: """
    s = "successes"
    print(Solution().maxFreqSum(s))