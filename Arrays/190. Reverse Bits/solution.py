class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = bin(n)[2:]

        left = 32 - len(binary)
        b = '0'*left + binary

        reversed_binary = "".join(list(reversed(b)))
        

        return int(reversed_binary, 2)



if __name__ == '__main__':
    """ Example 1: """
    n = 43261596
    print(Solution().reverseBits(n))


    """ Example 2: """
    n = 2147483644
    print(Solution().reverseBits(n))