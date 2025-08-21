from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        res = {}

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                res[str(arr[i]) + "/" +str(arr[j])] = arr[i] / arr[j]
        
        ans = list(dict(sorted(res.items(), key=lambda item: item[1])).keys())

        return [int(x) for x in ans[k-1].split("/")]
    

if __name__ == '__main__':
    """ Example 1: """
    arr = [1,2,3,5]
    k = 3
    print(Solution().kthSmallestPrimeFraction(arr, k))