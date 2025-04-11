import string

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        letters = string.ascii_lowercase

        indixes = {letters[i]:i for i in range(len(letters))}

        index = {i:letters[i] for i in range(len(letters))}
        
        substrings = [s[i:i+k] for i in range(0, len(s), k)]

        res = []

        for s in substrings:
            row = []
            for i in range(len(s)):
                row.append(indixes[s[i]])
            
            res.append(index[sum(row) % 26])
        
        return "".join(res)


if __name__ == '__main__':

    """ Example 1: """
    s = "abcd"
    k = 2
    print(Solution().stringHash(s, k))