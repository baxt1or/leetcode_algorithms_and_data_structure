from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = []
        
        count = Counter(words[0])

        for ch in count:
            min_base = min(w.count(ch) for w in words)

            res.extend([ch]*min_base)
        
        return res
            
            

if __name__ == '__main__':
    """ Example 1: """
    words = ["cool", "lock", "cook"]
    print(Solution().commonChars(words))


    """ Example 2: """
    words = ["bella","label","roller"]
    print(Solution().commonChars(words))