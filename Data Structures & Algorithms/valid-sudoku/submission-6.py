from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_sets = [[set() for _ in range(3)] for _ in range(3)]
        line_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]

        line = 0
        while line < 9:
            col = 0
            while col < 9:
                char = board[line][col]
                if char != ".":
                    #print(f"Checking {char} at {line},{col}")
                    if char in line_sets[line]:
                        #print(f"{char} is already in line {line}")
                        return False
                    line_sets[line].add(char)
                    #print(f"adding {char} to line {line}")

                    if char in col_sets[col]:
                        #print(f"{char} is already in colum {col}")
                        return False
                    col_sets[col].add(char)
                    #print(f"adding {char} to col {col}")

                    if char in square_sets[line // 3][col // 3]:
                        #print(f"{char} is already in square {line//3},{col//3}")
                        return False
                    square_sets[line // 3][col // 3].add(char)
                col += 1
            line += 1 
        return True