from typing import List, defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        groups = defaultdict(list)

        for i, id in enumerate(groupSizes):

            groups[id].append(i)
        
        group = []

        for key, ids in groups.items():
            if len(ids) > key:
                for i in range(0,len(ids),key):
                    group.append(ids[i:i+key])
            
            else:
                group.append(ids)
        
        return group

if __name__ == '__main__':

    """ Example 1: """
    groupSizes = [3,4,3,3,4,4,3,4,3,3]
    print(Solution().groupThePeople(groupSizes))


    """ Example 2: """
    groupSizes = [2,2,1,1,1,1,1,1]
    print(Solution().groupThePeople(groupSizes))