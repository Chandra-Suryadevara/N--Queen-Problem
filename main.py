from ChessBoard import ChessBoard
from NQueenSolver import NQueenSolver

number1 = input("Enter the size of Chess Board : ")
number = int(number1)
Board = ChessBoard(number,number)

QueenSolver = NQueenSolver(number)
QueenSolver.solveNQProblem(Board)