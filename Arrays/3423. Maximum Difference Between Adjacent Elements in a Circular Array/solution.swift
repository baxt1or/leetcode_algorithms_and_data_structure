
class Solution {
    func maxAdjacentDistance(_ nums: [Int]) -> Int {
        
        let n : Int = nums.count
        
        let diff = abs(nums[0] - nums[n-1])
        
        var max_element : Int = 0
        
        for i in 0..<n-1{
            max_element = max(max_element, abs(nums[i] - nums[i+1]))
        }
        
        return max(diff, max_element)
    }
}

let nums : [Int] = [-4,-2,-3]

print(Solution().maxAdjacentDistance(nums))