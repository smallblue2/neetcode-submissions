func twoSum(nums []int, target int) []int {
    memory := make(map[int]int)

    for idx, num := range nums {
        diff :=  target - num
        found, ok := memory[diff]
        if ok {
            return []int{found, idx}
        }
        memory[num] = idx
    }
    return nil
}
