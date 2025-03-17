class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        sum_of_digit = sum([int(s) for s in str(x)])

        return sum_of_digit if x % sum_of_digit == 0 else -1



if __name__ == '__main__':

    """ Example 1: """
    x = 18
    print(Solution().sumOfTheDigitsOfHarshadNumber(x))