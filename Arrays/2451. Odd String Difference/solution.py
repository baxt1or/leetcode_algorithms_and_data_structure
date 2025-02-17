from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:

        def dff(word):
            vocab = {chr(i+97):i for i in range(26)}
            res = []

            for i in range(len(word)-1):
                diff = vocab[word[i+1]] - vocab[word[i]]
                res.append(diff)
            return res
        
        seen = []
        res = []

        diffs = {i:dff(words[i]) for i in range(len(words))}

        for val in diffs.values():
            if val in seen:
                res.append(val)
            seen.append(val)
        
        return words[[key for key, val in diffs.items() if val not in res][0]]


if __name__ == "__main__":
     
    """ Example 1: """
    words = ["dtzca","dtzca","dtzca","yqyyo","dtzca","dtzca"]
    print(Solution().oddString(words))