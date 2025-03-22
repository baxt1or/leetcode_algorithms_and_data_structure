from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        N = len(votes[0]) 
        all_teams = list(set(votes[0]))    

        ranks = {team: [0] * N for team in all_teams}

        for s in votes:
            for rank, team in enumerate(s):
                ranks[team][rank] -= 1
        

        ranks = dict(sorted(ranks.items(), key=lambda item: (item[1], item[0])))

        return "".join(ranks.keys())
                

if __name__ == '__main__':
    
    """ Example 1: """
    votes = ["WXYZ","XYZW"]
    print(Solution().rankTeams(votes))


    """ Example 2: """
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    print(Solution().rankTeams(votes))

