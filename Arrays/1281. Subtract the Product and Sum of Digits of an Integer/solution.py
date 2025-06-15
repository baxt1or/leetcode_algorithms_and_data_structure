class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        

        product = 1
        total = 0

        for x in str(n):
            product *= int(x)
            total += int(x)
        
        return product-total


if __name__ == '__main__':

    """ Example 1: """
    n = 234
    print(Solution().subtractProductAndSum(n))