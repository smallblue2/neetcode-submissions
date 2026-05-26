func productExceptSelf(nums []int) []int {
    out := make([]int, len(nums))
    zero_positions := make(map[int]bool)

    // Collect them first
    sum_total := 1
    for i, num := range nums {
        if num == 0 {
            zero_positions[i] = true
            continue
        }
        sum_total *= num
    }

    // Divide
    for i, num := range nums {
        if _, ok := zero_positions[i]; ok {
            if len(zero_positions) > 1 {
                out[i] = 0
            } else {
                out[i] = sum_total
            }
        } else if len(zero_positions) != 0 {
            out[i] = 0
        } else {
            out[i] = sum_total / num
        }
    }

    return out
}
