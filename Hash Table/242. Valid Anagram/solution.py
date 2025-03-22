
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.get_frequency(s) == self.get_frequency(t)
    
    def get_frequency(self, s:str):

        frequency = {}

        for c in s:
            frequency[c] = frequency.get(c, 0)+1
        
        return frequency
        



if __name__ == '__main__':

    """ Example 1: """
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))