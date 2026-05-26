func groupAnagrams(strs []string) [][]string {
    groups := make(map[string][]string)
    for _, word := range strs {
        // Turn it into a slice of runes
        split := strings.Split(word, "")
        // Sort it
        sort.Strings(split)
        // Join it back together again
        sorted := strings.Join(split, "")

        subarr, ok := groups[sorted]
        if !ok {
            groups[sorted] = []string{word}
        } else {
            groups[sorted] = append(subarr, word)
        }
    }

    // Turn into 
    out := [][]string{}
    for _, v := range groups {
        out = append(out, v)
    }

    return out
}
