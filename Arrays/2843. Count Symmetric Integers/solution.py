
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        count = 0
         
        def is_symmetric(num):

            str_num = str(num)

            if len(str_num) % 2 != 0:
                return False

            num = [int(n) for n in str_num]
            mid = len(num) // 2

            return sum(num[:mid]) == sum(num[mid:])
        

        for n in range(low, high+1):

            if is_symmetric(n):
                count+=1
        
        return count


if __name__ == '__main__':

    """ Example 1: """
    low = 1
    high = 100
    print(Solution().countSymmetricIntegers(low, high))