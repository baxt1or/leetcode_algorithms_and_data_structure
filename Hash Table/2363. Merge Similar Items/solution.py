from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        count = {}

        for row in items1:
            count[row[0]] = row[1]
        
        for row in items2:
            if row[0] in count.keys():
                count[row[0]] = row[1] + count[row[0]]
            else:
                count[row[0]] = row[1]
        
        return sorted([[key, val] for key, val in count.items()], key=lambda item: item[0])

        
if __name__ == "__main__":
    items1 = [[1,3],[2,2]]
    items2 = [[7,1],[2,2],[1,4]]

    print(Solution().mergeSimilarItems(items1=items1, items2=items2))