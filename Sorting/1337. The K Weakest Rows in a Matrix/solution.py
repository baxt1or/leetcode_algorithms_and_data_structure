from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []

        for row in mat:
            res.append(row.count(1))
        
        ans = {i:r for r, i in zip(res,range(len(mat)))}

        result = dict(sorted(ans.items(), key=lambda item: item[1]))

        return list(result.keys())[:k]


if __name__ == "__main__":

    mat = [[1,1,0,0,0],
           [1,1,1,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0],
          [1,1,1,1,1]], 
    k = 3

    # Output: [2,0,3]
    Solution().kWeakestRows(mat, k)