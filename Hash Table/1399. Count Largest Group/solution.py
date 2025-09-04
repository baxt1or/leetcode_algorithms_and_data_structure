from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        nums = list(range(1, n+1))

        res = defaultdict(list)

        for i in range(len(nums)):
            r = sum([int(x) for x in str(nums[i])])
            res[r].append(nums[i])
            
        largest = len(res[max(res, key=lambda k: len(res[k]))])

        return len([key for key, val in res.items() if len(val) == largest])



if __name__ == '__main__':
    """ Example 1: """
    n = 2
    print(Solution().countLargestGroup(n))


    """ Example 2: """
    n = 13
    print(Solution().countLargestGroup(n))