class Solution:
    def groupAnagrams(self, strs ) :

        res = {}

        for word in strs:
            sorted_word = sorted(word)
            key = "".join(sorted_word)

            if key not in res:
                res[key] = [word]
            else:
                res[key].append(word)
        
        return res.values()

     
if __name__ == '__main__':

    """ Example 1: """
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))