import assignment5 as solver
import itertools

if __name__ == '__main__':

    print("Soduku Solver")
    csp = solver.create_sudoku_csp("boards/easy.txt")
    print(csp.variables)
    print(csp.domains)
    print("Constraints")
    print(csp.constraints)

    solution = csp.backtracking_search()
    if solution:
        solver.print_sudoku_solution(solution)
    else:
        print("No solution")