# N-Queen Puzzle with Backtracking CSP

This is a Python implementation of the N-Queen Puzzle using the Backtracking algorithm and Constraint Satisfaction Problem (CSP) approach. The N-Queen Puzzle is a classic problem in computer science and mathematics, where the goal is to place N queens on an NxN chessboard in such a way that no two queens threaten each other.

## Backtracking

Backtracking is a general algorithmic technique used to find solutions to problems by incrementally building candidates and abandoning them when they are deemed to be invalid. It works by exploring all possible configurations in a systematic way, eliminating branches of the search tree that are guaranteed to lead to invalid solutions.

## Constraint Satisfaction Problem (CSP)

A Constraint Satisfaction Problem is a mathematical problem defined as a set of objects whose state must satisfy several constraints. In the N-Queen Puzzle, the constraints are that no two queens can be placed in the same row, column, or diagonal.

## Usage

To run the N-Queen Puzzle solver, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Download or clone this repository.
3. Open a terminal or command prompt and navigate to the directory containing the `main.py` file.
4. Run the following command to execute the program:

```bash
python nqueen.py
```

5. You will be prompted to enter the value of N, which represents the number of queens and the size of the chessboard.
6. The program will attempt to find a valid solution and display the board configuration if one exists. If no solution is found, an appropriate message will be displayed.

## Implementation Details

The `main.py` file contains the implementation of the N-Queen Puzzle solver using the backtracking CSP approach. The main function, `solve_n_queen`, takes the value of N as input and returns the board configuration as a list of lists.

The solver uses a recursive backtracking algorithm to explore all possible configurations. It starts by placing a queen in the first row and then recursively explores all possible positions in the next row. If a position is found where a queen can be placed without violating the constraints, the algorithm moves on to the next row. If no valid position is found, it backtracks to the previous row and explores other positions. This process continues until a valid solution is found or all possible configurations are exhausted.

The program uses a helper function, `is_valid`, to check if a queen can be placed in a given position without conflicting with any other queens on the board. The function checks the row, column, and diagonal constraints to determine the validity of a position.

## Example

Here's an example of running the N-Queen Puzzle solver with N = 4:

```bash
python main.py
Enter the value of N: 4

Solution found:
- Q - -
- - - Q
Q - - -
- - Q -
```

In this example, the solver found a valid solution where four queens are placed on a 4x4 chessboard without threatening each other.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

This implementation was created by [Your Name]. It is based on the backtracking and CSP concepts widely used in solving the N-Queen Puzzle.

## REFERENCE

geeksforgeeks.org/n-queen-problem-backtracking-3/
