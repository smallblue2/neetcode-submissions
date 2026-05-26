// N = dimension of square

// O ( N ^ 2 )
// S ( N ^ 2 )

func isValidSudoku(board [][]byte) bool {
    board_len := len(board)
    horizontal := make([]map[byte]bool, board_len) // S ( N * N )
    vertical := make([]map[byte]bool, board_len) // S ( N * N )
    grids := make([][]map[byte]bool, board_len) // S ( N * N )

    for i, _ := range board { // O ( N )
        horizontal[i] = make(map[byte]bool)
        for j, num := range board[i] { // O ( N )
            if check_map := vertical[j]; check_map == nil {
                vertical[j] = make(map[byte]bool)
            }

            grid_y := i / 3
            grid_x := j / 3
            if check_slice := grids[grid_y]; check_slice == nil {
                grids[grid_y] = make([]map[byte]bool, board_len / 3)
            }
            if check_map := grids[grid_y][grid_x]; check_map == nil {
                grids[grid_y][grid_x] = make(map[byte]bool, board_len)
            }

            if (num == '.') {
                continue
            }

            _, in_grid := grids[grid_y][grid_x][num]
            _, in_horizontal := horizontal[i][num]
            _, in_vertical := vertical[j][num]
            if in_grid || in_horizontal || in_vertical { 
                fmt.Printf("INVALID: grid: %v horiz: %v vert: %v\n", in_grid, in_horizontal, in_vertical)
                fmt.Printf("line: %d, square: %d, grid: (%d, %d)\n", i, j, grid_x, grid_y)
                return false
            }

            grids[grid_y][grid_x][num] = true
            horizontal[i][num] = true
            vertical[j][num] = true
        } 
    }
    return true
}
