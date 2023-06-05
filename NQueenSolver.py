class NQueenSolver:
  def __init__(self,n):
     global N
     N = n
   

  def isSafer(self,board, row, col):
 
    
     for i in range(col):
        if board[row][i] == 1:
            return False
 
   
     for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    
     for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
     return True
 
 
  def solveNQUtillthis(self,board, col):
 
    
    if col >= N:
        return True

    for i in range(N):
 
        if self.isSafer(board, i, col):
 
            board[i][col] = 1
 
            if self.solveNQUtil(board, col + 1) == True:
                return True
 
            
            board[i][col] = 0
 
    
    return False
 
 

  def solveNQProblem(self,board):
    
 
    if self.solveNQUtillthis(board.get_board(), 0) == False:
        print("Solution does not exist")
        return False
 
    board.print_board()
    return True
 
 
 


