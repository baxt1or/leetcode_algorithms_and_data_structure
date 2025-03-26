from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
                
        res = []
        row = []

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                res.append(s[i]+s[j])
                break
        
        valid_nums = set([key for key, val in Counter(s).items() if int(key) == val])

        for pair in res:
            if all(c in valid_nums for c in pair) and len(set(pair)) > 1:
                row.append(pair)
        
        return "" if not row else row[0]
    

if __name__ == '__main__':

    """ Example 1: """
    s = "9212"
    print(Solution().findValidPair(s))