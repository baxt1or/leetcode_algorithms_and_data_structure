
class Solution {
    func findPermutationDifference(_ s: String, _ t: String) -> Int {
        
        var sCount : [Character : Int] = [:]
        var tCount : [Character : Int] = [:]
        
        for (i, c) in s.enumerated(){
            
            sCount[c] = i
        
        }
        
        for (i, c) in t.enumerated(){
            tCount[c] = i
        }
        
        var total = 0
 
        for c in String(s.sorted()) {
            
            if let sIndex = sCount[c], let tIndex = tCount[c] {
                
                let diff = abs(sIndex - tIndex)
                total += diff
                
            }
            
        }
        
        return total
    }
}


// Example 1:
let s : String = "abcde"
let t : String = "edbac"

print(Solution().findPermutationDifference(s, t))

// Example 2:
let s : String = "abc"
let t : String = "bac"

print(Solution().findPermutationDifference(s,t))