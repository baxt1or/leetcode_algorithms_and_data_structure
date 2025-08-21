
class Solution {
    func permute(_ nums: [Int]) -> [[Int]] {
        
        
        let n = nums.count
        var ans : [[Int]] = []
        var sol : [Int] = []
        
        func backtrack() {
            
            if sol.count == n {
                let newSol = sol
                ans.append(newSol)
                return
            }
            
            for x in nums {
                if !sol.contains(x) {
                    sol.append(x)
                    backtrack()
                    sol.popLast()
                }
            }
            
        }
        
        backtrack()
        
        return ans
    }
}

let s = Solution()

let nums : [Int] = [1, 2,3]
print(s.permute(nums))
