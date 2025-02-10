from typing import List

class Solution:
    def __init__(self):
        self.first_row = set('qwertyuiop')
        self.second_row = set('asdfghjkl')
        self.third_row = set('zxcvbnm')
    
    def findWords(self, words: List[str]) -> List[str]:
        
        res = []

        for word in words:
            set_word = set(word.lower())
            if set_word.issubset(self.first_row):
                res.append(word)
            if set_word.issubset(self.second_row):
                res.append(word)
            if set_word.issubset(self.third_row):
                res.append(word)
        return res


if __name__ == "__main__":

    words = ["Hello","Alaska","Dad","Peace"]
    print(Solution().findWords(words))