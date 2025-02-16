class Solution:
    def validWordSquare(self, words) -> bool:
        
        rows = [list(word) for word in words]

        cols = []

        max_len = max(len(word) for word in words)

        for c in range(max_len):
            row = []

            for r in range(len(words)):
                if c < len(words[r]):
                    row.append(words[r][c])
            
            cols.append(row)
        
        return cols == rows


if __name__ == '__main__':

    """ Example 1: """
    words = ["abcd","bnrt","crm","dt"]
    print(Solution().validWordSquare(words))