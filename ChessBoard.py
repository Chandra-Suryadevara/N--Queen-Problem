

class ChessBoard:
    def __init__(self,rows,cols):
      self.rows1=rows
      self.cols1=cols
      self.tiles = [[0 for _ in range(rows)] for _ in range(cols)]



    def print_board(self):
     for i in range(self.rows1):
        for j in range(self.cols1):
            print(self.tiles[i][j], end=" ")
        print()


    def get_board(self):
        return self.tiles
