// N = len(nums)
// M = # unique items in 'nums'

func topKFrequent(nums []int, k int) []int {

    freqs := make(map[int]int)
    for _, num := range nums { // O ( N )
        freqs[num] = freqs[num] + 1
    }

    sorted_freqs := make([]int, 0, len(freqs)) // O ( M )
    for key, _ := range freqs {
        sorted_freqs = append(sorted_freqs, key)
    }

    sort.Slice(sorted_freqs, func (i, j int) bool { // O ( M log M )
        return freqs[sorted_freqs[i]] > freqs[sorted_freqs[j]]
    })

    return sorted_freqs[:k]
}

// O (N + M + MlogM)
