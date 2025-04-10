import string

class Solution:
    def reverseDegree(self, s: str) -> int:
        
        letters = list(reversed(string.ascii_lowercase))
        
        reversed_indixes = {letters[i]:i+1 for i in range(0,26)}
        
        return sum([reversed_indixes[s[i]]*(i+1) for i in range(len(s))])
            

if __name__ == '__main__':

    """ Example 1: """
    s = 'abc'
    print(Solution().reverseDegree(s))

    """ Example 2: """
    s = 'zaza'
    print(Solution().reverseDegree(s))