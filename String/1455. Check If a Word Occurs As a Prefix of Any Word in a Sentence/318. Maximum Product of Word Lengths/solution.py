from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n = len(words)
        masks = [0] * n
        lengths = [0] * n

        for i, word in enumerate(words):
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            masks[i] = mask
            lengths[i] = len(word)
        
        max_val = 0

        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    max_val = max(max_val, lengths[i] * lengths[j])
        
        return max_val
    

if __name__ == '__main__':
    """ Example 1: """
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(Solution().maxProduct(words=words))


    """ Example 2: """
    words = ["a","aa","aaa","aaaa"]
    print(Solution().maxProduct(words=words))