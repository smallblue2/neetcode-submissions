func isAnagram(s string, t string) bool {
    memory := make(map[rune]int)
    for _, letter := range s {
        memory[letter] = memory[letter] + 1
    }
    for _, letter := range t {
        memory[letter] = memory[letter] - 1
    }
    for _, v := range memory {
        if v != 0 {
            return false
        }
    }
    return true

}
