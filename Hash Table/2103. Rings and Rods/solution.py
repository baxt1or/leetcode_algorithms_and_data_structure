from typing import defaultdict

class Solution:
    def countPoints(self, rings: str) -> int:
        
        res = []
        count = defaultdict(list)

        for i in range(len(rings)):
            if rings[i].isdigit():
                count[rings[i]].append(rings[i-1])
                
        
        res = 0

        for k, v in count.items():
            if len(set(v)) >=3:
                res +=1
        
        return res


if __name__ == '__main__':
    """ Example 1: """
    rings = "B0R0G0R9R0B0G0"
    print(Solution().countPoints(rings))

    """ Example 2: """
    rings = "B0B6G0R6R0R6G9"
    print(Solution().countPoints(rings))

    """ Example 3: """
    rings = "G4"
    print(Solution().countPoints(rings))