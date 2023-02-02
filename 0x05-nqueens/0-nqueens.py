#!/usr/bin/python3
"""
N-Queens Algorithms
"""
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(args[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    row = 0
    col = 0
    solutions = []
    placed_queens = []
    stop = False

    # iterating through rows and columns
    while row < n:
        back_track = False
        while col < n:
            # check if current column is safe
            safe = True
            for cord in placed_queens:
                c = cord[1]
                if (c == col or c + (row-cord[0]) == col or
                        c - (row-cord[0]) == col):
                    safe = False
                    break

            if not safe:
                if col == n - 1:
                    back_track = True
                    break
                col += 1
                continue

            # place queen
            cords = [row, col]
            placed_queens.append(cords)
            # if it is the last row
            # append solution and reset all to last unfinished row
            # and last safe column in that row
            if row == n - 1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        row = cord[0]
                        col = cord[1]
                for i in range(n - row):
                    placed_queens.pop()
                if row == n - 1 and col == n - 1:
                    placed_queens = []
                    stop = True
                row -= 1
                col += 1
            else:
                col = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if back_track:
            row -= 1
            while row >= 0:
                col = placed_queens[row][1] + 1
                del placed_queens[row]
                if col < n:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val)
        else:
            print(val)
