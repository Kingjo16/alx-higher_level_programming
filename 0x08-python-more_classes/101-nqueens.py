#!/usr/bin/python3

import sys


def new_board(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def nqueens_sol(board, row, n, solutions):
    if row == n:
        solutions.append([(i, board[i]) for i in range(n)])
        return

    for col in range(n):
        if new_board(board, row, col, n):
            board[row] = col
            nqueens_sol(board, row + 1, n, solutions)


def sol_print(solutions):
    for solution in solutions:
        print(solution)
    print()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])

    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    nqueens_sol(board, 0, N, solutions)
    sol_print(solutions)


if __name__ == "__main__":
    main()
