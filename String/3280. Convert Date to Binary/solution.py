class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        return bin(year)[2:] + '-' + bin(month)[2:] + '-' + bin(day)[2:]


if __name__ == '__main__':
    """ Example 1: """
    date = "2080-02-29"
    print(Solution().convertDateToBinary(date))
