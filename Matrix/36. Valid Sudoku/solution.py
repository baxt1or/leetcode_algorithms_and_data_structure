from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

      count_row = 0
      count_col = 0
      sub_row = 0


      n = set([str(x) for x in range(1, 10)])

      for row in board:
        a = [x for x in row if x.isdigit()]
        if len(a) == len(set(a)):
           count_row+=1  

      for i in range(len(board[0])):
        row = []
        for r in board:
          if r[i].isdigit():
            row.append(r[i])
        if len(row) == len(set(row)):
          count_col +=1

      sub_boxes = self.get_subboxes(board)

      for row in sub_boxes:
        a = [str(x) for x in row if x.isdigit()]
        if len(a) == len(set(a)):
          sub_row+=1
      
      return count_row == count_col == sub_row == 9
    

      
    def get_subboxes(self, matrix):
      sub_boxes = []

      for i in range(0, 9, 3):
        for j in range(0, 9, 3):
          box = [matrix[x][y] for x in range(i, i+3) for y in range(j, j+3)]
          sub_boxes.append(box)
      return sub_boxes

if __name__ == "__main__":
  
  """ Example 1: """

  board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
  
  print(Solution().isValidSudoku(board))

  """ Example 2: """
  
  board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

  print(Solution().isValidSudoku(board))