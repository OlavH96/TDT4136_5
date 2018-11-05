import assignment5
from Sudoku import *
if __name__ == '__main__':


    print("Soduku Solver")
    csp = assignment5.create_sudoku_csp("boards/easy.txt")
    print(csp.variables)
    print(csp.domains)
    print(csp.constraints)

    assignment = csp.backtracking_search()
    print(assignment)
    assignment5.print_sudoku_solution(assignment)