

class Solution {
    func isValid(_ s: String) -> Bool {
        
        var stack : [Character] = []
        
        let brakets : [Character : Character] = ["}":"{", "]":"[", ")" : "("]
        
        
        for c : Character in s {
            if brakets.values.contains(c) {
                stack.append(c)
            }
            else if brakets.keys.contains(c) {
                if stack.isEmpty || stack.popLast() != brakets[c] {
                    return false
                }
            }
        }
        
        return stack.count == 0
    }
}




let s = "()[]{}"

print(Solution().isValid(s))
