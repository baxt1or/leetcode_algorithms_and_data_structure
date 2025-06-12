class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        first = abs(z-x)
        second = abs(z-y)

        
        return 1 if first < second else 0 if first == second else 2

if __name__ == '__main__':

    """ Example 1: """
    x = 2
    y = 5
    z = 6
    print(Solution().findClosest(x, y, z))


    """ Example 2: """
    x = 1
    y = 5
    z = 3
    print(Solution().findClosest(x, y, z))