from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        table = {}

        for row in orders:
            table[(row[1], row[2])] = table.get((row[1], row[2]), 0)+1
        
        table_names = ["Table"] + sorted(set([row[2] for row in orders]))
        table_numbers = sorted(list(set([int(row[1]) for row in orders])))

        result_table = [table_names]

        for num in table_numbers:
            row = [str(num)]
            for name in table_names[1:]:
                row.append(str(table.get((str(num),name), 0)))
            result_table.append(row)
        return result_table


if __name__ == "__main__":
    """ Example 1:"""
    orders = [["David","3","Ceviche"],
              ["Corina","10","Beef Burrito"],
              ["David","3","Fried Chicken"],
              ["Carla","5","Water"],
              ["Carla","5","Ceviche"],
              ["Rous","3","Ceviche"]]
    
    """ Explanation:
        The displaying table looks like:
        Table,Beef Burrito,Ceviche,Fried Chicken,Water
        3    ,0           ,2      ,1            ,0
        5    ,0           ,1      ,0            ,1
        10   ,1           ,0      ,0            ,0
        For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
        For the table 5: Carla orders "Water" and "Ceviche".
        For the table 10: Corina orders "Beef Burrito". 
    """

    print(Solution().displayTable(orders))

    """ Example 2: """
    orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
    print(Solution().displayTable(orders))

    """ Example 3: """
    orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
    print(Solution().displayTable(orders))