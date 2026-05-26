func topKFrequent(nums []int, k int) []int {

    freq_map := make(map[int]int)
    for _, num := range nums { // O ( N )
        freq_map[num] = freq_map[num] + 1
    }

    fmt.Printf("OK")
    freq_arr := make([][]int, len(nums) + 1)
    for key, val := range freq_map {
        freq_arr[val] = append(freq_arr[val], key)
    }
    fmt.Printf("KO\n")

    out := make([]int, 0, k)

    fmt.Printf("%v\n", freq_arr)

    for i := len(freq_arr) - 1; i > 0; i-- {
        fmt.Printf("%d: %d\n", i, len(freq_arr[i]))
        if len(out) >= k {
            break
        }
        if len(freq_arr[i]) != 0 {
            out = append(out, freq_arr[i]...)
        }
    }

    return out[:k]
}

