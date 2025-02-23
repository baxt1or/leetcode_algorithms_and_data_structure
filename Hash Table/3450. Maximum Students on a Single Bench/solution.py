from typing import List, defaultdict 

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        
        benchs = defaultdict(set)

        for row in students:
            benchs[row[1]].add(row[0])

        max_students = 0

        for key, vals in benchs.items():
            max_students = max(max_students, len(vals))
        
        return max_students


if __name__ == '__main__':

    """ Example 1: """
    students = [[1,2],[2,2],[3,3],[1,3],[2,3]]
    print(Solution().maxStudentsOnBench(students))