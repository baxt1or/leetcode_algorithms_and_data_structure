class Solution:
    def findComplement(self, num: int) -> int:
        
        binary = bin(num)[2:]

        res = []

        for c in binary:
            if c == '0':
                res.append('1')
            else:
                res.append('0')
        
        return int("".join(res), 2)



if __name__ == '__main__':
    """ Example 1: """
    num = 5
    print(Solution().findComplement(num))


    """ Example 2: """
    num = 1
    print(Solution().findComplement(num))