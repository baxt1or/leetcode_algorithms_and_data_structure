from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        res = []
        
        def f(s):
            return s.count(min(s))
        
        word_frequency = [f(word) for word in words]

        for q in queries:
            freq = f(q)
            count = 0
            for w in word_frequency:
                if w > freq:
                    count+=1
            res.append(count)
        
        return res
    

if __name__ == '__main__':  

    """ Example 1: """
    queries = ["bbb","cc"]
    words = ["a","aa","aaa","aaaa"]
    print(Solution().numSmallerByFrequency(queries,words))