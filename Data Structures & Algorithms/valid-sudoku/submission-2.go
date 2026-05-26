// N = dimension of square

// O ( N ^ 2 )
// S ( N )

func isValidSudoku(board [][]byte) bool {
    board_len := len(board)
    rows := make([]int, board_len) // S ( N )
    cols := make([]int, board_len) // S ( N )
    squares := make([]int, board_len) // S ( N )

    for y, _ := range board { // O ( N )
        for x, _ := range board[y] { // O ( N )
            digit := board[y][x]
            if digit == '.' {
                continue
            }
            digit = digit - '1'

            row := y / 3
            col := x / 3
            square := (row * 3) + col

            mask := 1 << digit

            row_check := rows[y] & mask
            cols_check := cols[x] & mask
            square_check := squares[square] & mask

            if row_check == mask || cols_check == mask || square_check == mask {
                return false
            }

            rows[y] |= mask
            cols[x] |= mask
            squares[square] |= mask
        }
    }
    return true
}
