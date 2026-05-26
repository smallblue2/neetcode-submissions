func groupAnagrams(strs []string) [][]string {
    freq_map := make(map[[27]rune][]string)
    base := rune('a')
    for _, word := range strs { // O ( n )
        signature := [27]rune{}
        for _, letter := range word { // O ( m )
            signature[rune(letter) - base] += 1
        }
        
        subarr, ok := freq_map[signature]
        if !ok {
            freq_map[signature] = []string{word}
        } else {
            freq_map[signature] = append(subarr, word)
        }
    }

    // Turn into slice
    out := [][]string{}
    for _, v := range freq_map { // O(K)
        out = append(out, v)
    }

    return out
}

// O ( K + N * M  )); K = # anagram groups; N = # input strings; M = length of string
