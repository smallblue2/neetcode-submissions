// N = # nums
// M = max frequency

func topKFrequent(nums []int, k int) []int {

    freq_map := make(map[int]int)
    for _, num := range nums { // O ( N )
        freq_map[num] = freq_map[num] + 1
    }

    freq_arr := make([][]int, len(nums) + 1)
    for key, val := range freq_map { // O ( M )
        freq_arr[val] = append(freq_arr[val], key)
    }

    out := make([]int, 0, k)

    for i := len(freq_arr) - 1; i > 0; i-- { // O ( M )
        if len(out) >= k {
            break
        }
        if len(freq_arr[i]) != 0 {
            out = append(out, freq_arr[i]...)
        }
    }

    return out[:k]
}


// O (N + M); but N >= M, O ( N )