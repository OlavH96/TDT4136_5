import assignment5 as solver


def solve(board, should_print=False):
    csp = solver.create_sudoku_csp(board)
    solution = csp.backtracking_search()
    if should_print:
        print("Solution for", board)
        solver.print_sudoku_solution(solution)
        print("Number of backtrack calls", csp.num_backtrack_calls)
        print("Number of failure returns", csp.num_failures)
        print()
    return True if solution else False


if __name__ == '__main__':
    boards = ["boards/easy.txt", "boards/medium.txt", "boards/hard.txt", "boards/veryhard.txt"]

    all_solved = all(map(lambda board: solve(board, should_print=True), boards))
    print("Solved all boards?", all_solved, "\n")
