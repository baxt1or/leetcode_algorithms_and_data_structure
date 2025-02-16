class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split(" ")

        res = []

        for i in range(len(sentence)):
            if sentence[i].startswith(searchWord):
                return i+1
        
        return -1
    
    def is_prefix(self, word, prefix):

        if len(prefix) > len(word):
            return False

        for i in range(len(prefix)):
            if word[i] != prefix[i]:
                return False
        return True


if __name__ == '__main__':
     
    """ Example 1: """
    sentence = "i love eating burger"
    searchWord = "burg"
    print(Solution().isPrefixOfWord(sentence, searchWord))