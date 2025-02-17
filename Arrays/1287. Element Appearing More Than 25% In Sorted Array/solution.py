class Solution:
    def findSpecialInteger(self, arr) -> int:
        
        count = {}

        for n in arr:
            count[n] = count.get(n, 0)+1

        total = sum(count.values())

        for key, val in count.items():
            if val/total > 0.25:
                return key


if __name__ == '__main__':
    
    """ Example 1: """
    arr = [1,2,2,6,6,6,6,7,10]
    print(Solution().findSpecialInteger(arr=arr))