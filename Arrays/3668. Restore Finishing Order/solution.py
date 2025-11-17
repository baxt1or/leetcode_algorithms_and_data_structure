from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
                    
        friends_table = {x:i for i, x in enumerate(friends)}
        
        return [n for n in order if n in friends_table]


order = [3,1,2,5,4]
friends = [1,3,4]

# Output: [3,1,4]
print(Solution().recoverOrder(order, friends))