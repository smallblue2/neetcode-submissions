func hasDuplicate(nums []int) bool {
    seen := make(map[int]bool)
    for _, item := range nums {
        if seen[item] {
            return true
        }
        seen[item] = true
    }
    return false
}
