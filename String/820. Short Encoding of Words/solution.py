from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))  # Remove duplicates
        res = []
        
        words = sorted(words, key=len, reverse=True) 

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i].endswith(words[j]): 
                    res.append(words[j])
                    break
        
        return len("#".join([word for word in words if word not in res]) + "#")

if __name__ == '__main__':

    """ Example 1: """
    words = ["time","atime","btime"]
    print(Solution().minimumLengthEncoding(words))