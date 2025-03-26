import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        root = math.sqrt(num)

        if int(root*root) == num and int(root) == root:
            return True
        return False
    

if __name__ == '__main__':

    """ Example 1: """
    num = 14
    print(Solution().isPerfectSquare(num=num))