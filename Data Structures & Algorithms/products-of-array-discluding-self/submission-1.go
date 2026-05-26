// O ( N )
// N = # nums in input slice

func productExceptSelf(nums []int) []int {
    out := make([]int, len(nums))
    prefix := make([]int, len(nums))
    suffix := make([]int, len(nums))

    prefix[0], suffix[len(nums) - 1] = 1, 1

    // x * (product of everything to right)
    for i := len(nums) - 2; i >= 0; i-- {
        suffix[i] = nums[i + 1] * suffix[i + 1]
    }

    // (product of everything to left) * x
    for i := 1; i < len(nums); i++ {
        prefix[i] = nums[i - 1] * prefix[i - 1]
    }

    // Combine
    for i, _ := range nums {
        out[i] = prefix[i] * suffix[i]
    }

    return out
}
