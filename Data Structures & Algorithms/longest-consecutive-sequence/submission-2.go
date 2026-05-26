// N = len(nums)
// M = # unique numbers in nums; M < N

// O ( N + M ); M <= N; O ( N )
// S ( M ); M <= N; S ( N )

func longestConsecutive(nums []int) int {
    counter := make(map[int]*int) // S ( M )
    accounted_for := make(map[int]bool) // S ( M )

    for _, num := range nums { // O ( N )
        // Have we accounted for this number?
        if _, ok := accounted_for[num]; ok {
            // skip
            continue
        }

        // Check if we can go further with this
        pre_ptr, pre_ok := counter[num - 1]
        aft_ptr, aft_ok := counter[num + 1]
        // There is one before
        if pre_ok && aft_ok {
            *pre_ptr += *aft_ptr + 1
            counter[num + 1] = pre_ptr
            counter[num] = pre_ptr
        } else if pre_ok {
            *pre_ptr += 1
            counter[num] = pre_ptr
        } else if aft_ok {
            *aft_ptr += 1
            counter[num] = aft_ptr
        } else {
            // No chain to add to, create our own
            current_counter := new(int)
            *current_counter = 1
            counter[num] = current_counter
        }
        accounted_for[num] = true
    }

    max_count := 0
    for _, count := range counter { // O ( M )
        if *count > max_count {
            max_count = *count
        }
    }
    return max_count
}
