class Solution1 {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        
        for i in 0..<nums.count{
            for j in i+1..<nums.count{
                if nums[i] == nums[j]{
                    return true
                }
            }
        }
        
        return false
    }
}


class Solution2 {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        
        let count = nums.count
        let setCount = Set(nums).count
        
        if count == setCount{
            return false
        }else{
            return true
        }
    }
}

class Solution3 {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        
        var stack = Set<Int>()
        
        for num in nums{
            if stack.contains(num){
                return true
            }
            stack.insert(num)
        }
        
        return false
    }
}


let nums = [1,2,3,1]
print(Solution1().containsDuplicate(nums))
print(Solution2().containsDuplicate(nums))
print(Solution3().containsDuplicate(nums))

