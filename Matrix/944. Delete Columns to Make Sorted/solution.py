from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count = 0

        for c in range(len(strs[0])):
            row = []
            for r in strs:
                row.append(r[c])
            
            word = "".join(row)
            sorted_word = "".join(sorted(row))

            if word != sorted_word:
                count+=1

        return count

if __name__ == '__main__':

    sol = Solution()

    """ Example 1: """
    strs = ["cba","daf","ghi"]
    print(sol.minDeletionSize(strs=strs))


    """ Example 2: """
    strs = ["a","b"]
    print(sol.minDeletionSize(strs=strs))


    """ Example 3: """
    strs = ["zyx","wvu","tsr"]
    print(sol.minDeletionSize(strs=strs))