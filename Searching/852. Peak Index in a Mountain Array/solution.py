from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_value = max(arr)

        l, r = 0, len(arr)-1

        for i in range(len(arr)-1):
            if arr[i] == max_value and arr[i] > arr[i+1]:
                return i
        return -1


if __name__ == "__main__":
    arr = [0,10,5,2]
    print(Solution().peakIndexInMountainArray(arr))