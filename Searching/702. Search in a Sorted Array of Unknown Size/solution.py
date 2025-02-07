# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
   def get(self, index: int) -> int:
       pass

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        idx = 0
        res = []
        while reader.get(idx) < 2**31 - 1:
            res.append(reader.get(idx))
            idx+=1
        
        l, r = 0, len(res) - 1

        while l <= r:
            mid = (l+r) // 2

            if res[mid] == target:
                return mid
            elif res[mid] > target:
                r = mid -1
            else:
                l = mid+1
        return -1
    

if __name__ == "__main__":
    secret = [-1,0,3,5,9,12]
    target = 9 

    Solution().search(target)