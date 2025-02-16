from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        sentence = sentence.split(" ")
        

        for i in range(len(sentence)):
            for j in range(len(dictionary)):
                if self.is_prefix(sentence[i],dictionary[j]):
                    sentence[i] = dictionary[j]
        
        return " ".join(sentence)
    
    def is_prefix(self, word, prefix):

        if len(prefix) > len(word):
            return False
        
        for i in range(len(prefix)):
            if word[i] != prefix[i]:
                return False
        return True


if __name__ == '__main__':

    """ Example 1: """
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dictionary, sentence))


    """ Example 2: """
    dictionary = ["a","b","c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(Solution().replaceWords(dictionary, sentence))