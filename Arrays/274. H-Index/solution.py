from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        hs = list(range(1, len(citations)+1))

        ans = []

        for h in hs:
            res = 0
            for n in citations:
                if n >= h:

                    res+=1

            if res >= h:

               ans.append(res)                        
        
        return len(ans)
    


if __name__ == '__main__':
    """ Example 1: """
    citations = [3,0,6,1,5]
    print(Solution().hIndex(citations))

    """ Example 1: """
    citations = [1,3,1]
    print(Solution().hIndex(citations))

    """ Example 1: """
    citations  = [1]
    print(Solution().hIndex(citations))

    """ Example 1: """
    citations  = [1,1]
    print(Solution().hIndex(citations))