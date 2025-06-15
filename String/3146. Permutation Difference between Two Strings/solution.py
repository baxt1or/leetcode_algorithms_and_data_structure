class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = i 
            t_count[t[i]] = i 
        

        total = 0

        for c in sorted(s):
            
            diff = abs(s_count[c] - t_count[c])

            total += diff
        
        return total
    

if __name__ == '__main__':

    """ Example 1: """
    s = "abcde"
    t = "edbac"
    print(Solution().findPermutationDifference(s, t))

    """ Example 2: """
    s = "abcde"
    t = "edbac"
    print(Solution().findPermutationDifference(s,t))