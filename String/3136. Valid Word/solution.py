import string

class Solution:
    def isValid(self, word: str) -> bool:
        
        vowels = set('aeiouAEIOU')
        
        consonants = set(string.ascii_letters) - vowels

        digits = set('0123456789')

        has_vowels = False
        has_consonants = False
        

        if len(word) < 3:
            return False

        for c in word:
            if c in vowels:
                has_vowels = True
            elif c in consonants:
                has_consonants = True
            elif c not in digits:
                return False
            
        
        return has_vowels == has_consonants
            


if __name__ == '__main__':

    """ Example 1: """
    word = "234Adas"
    print(Solution().isValid(word))

    """ Example 2: """
    word = "3#H"
    print(Solution().isValid(word=word))