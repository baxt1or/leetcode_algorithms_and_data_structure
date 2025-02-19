from collections import Counter
from typing import List

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        items = [(val, labels) for val, labels in zip(values, labels)]

        items = sorted(items, key=lambda item:item[0], reverse=True)

        count = Counter()

        total = 0
        total_picked = 0

        for val, label in items:

            if total_picked < numWanted and count[label] < useLimit:
                total+=val
                total_picked+=1
                count[label] +=1

        return total

if __name__ == '__main__':

    """ Example 1: """
    values = [5,4,3,2,1]
    labels = [1,1,2,2,3]
    numWanted = 3
    useLimit = 1
    print(Solution().largestValsFromLabels(values, labels,numWanted, useLimit))