from collections import Counter 

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        

        target, freq =  Counter(target), Counter(s)

        res = []

        for c in 'code':
            if c in target and freq:
                res.append(freq[c] // target[c])
        
        return min(res) if res else 0





if __name__ == '__main__':
    
    """ Example 1: """

    s = "ilovecodingonleetcode"
    target = "code"
    print(Solution().rearrangeCharacters(s,target))