from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commons = list(set(list1).intersection(set(list2)))
        
        res = {}
        for s in commons:
            l1 = list1.index(s)
            l2 = list2.index(s)
            res[s] = l1+l2
        
        min_ = min(res.values())

        return [key for key, val in res.items() if val == min_]
        