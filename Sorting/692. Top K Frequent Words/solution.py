from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        words.sort()

        count = {}


        for word in words:
            count[word] = count.get(word, 0) + 1

        
        return [key for key in dict(sorted(count.items(), key=lambda item:item[1], reverse=True)).keys()][:k]


if __name__ == '__main__':

    """ Example 1: """

    words = ["i","love","leetcode","i","love","coding"]
    k = 3
    print(Solution().topKFrequent(words, k))