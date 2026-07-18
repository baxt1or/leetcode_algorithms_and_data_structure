class Solution:
    def removeZeros(self, n: int) -> int:

        res = ''

        while n != 0:
            if n % 10 != 0:
                res += str(n % 10)
            n = n // 10
        
        return int(res[::-1])




if __name__ == '__main__':
    """ Example 1 """
    n = 1020030
    print(Solution().removeZeros(n))


