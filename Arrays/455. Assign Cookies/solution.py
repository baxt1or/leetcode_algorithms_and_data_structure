from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):

            if s[cookie] >= g[child]:
                child +=1
            cookie +=1
        

        return child
    


if __name__ == '__main__':

    """ Example 1: """
    g = [1,2,3]
    s = [1,1]
    print(Solution().findContentChildren(g, s))


    """ Example 2: """
    g = [1,2]
    s = [1,2,3]
    print(Solution().findContentChildren(g, s))