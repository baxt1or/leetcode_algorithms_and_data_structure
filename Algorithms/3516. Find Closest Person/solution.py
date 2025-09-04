class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        
        p1 = abs(x-z)
        p2 = abs(y-z)

        if p1 > p2:
            return 2
        elif p1 == p2:
            return 0
        else:
            return 1 
        


if __name__ == '__main__':
    """ Example 1: """
    x = 2
    y = 7
    z = 4
    print(Solution().findClosest(x, y, z))

    """ Example 2: """
    x = 2
    y = 5
    z = 6
    print(Solution().findClosest(x, y, z))

    """ Example 3: """
    x = 1
    y = 5
    z = 3
    print(Solution().findClosest(x, y, z))