import string

class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        vowels = set('aeiou')
        consonants = set([c for c in set(string.ascii_lowercase) if c not in vowels])

        ans = []

        for word in sentence.split():
            if word[0].lower() in vowels:
                ans.append(word+'ma')
            elif word[0].lower() in consonants:
                ans.append(word[1:]+word[0] +'ma')
            else:
                ans.append(word)
        
        res = []

        for i in range(1, len(ans)+1):
            res.append(ans[i-1] + i*'a')
            

        return " ".join(res)




if __name__ == '_name__':
    """ Example 1: """
    sentence = "I speak Goat Latin"
    # Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    print(Solution().toGoatLatin(sentence=sentence))
    
    """ Example 2: """
    sentence = "The quick brown fox jumped over the lazy dog"
    # Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa 
    # overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    print(Solution().toGoatLatin(sentence=sentence))