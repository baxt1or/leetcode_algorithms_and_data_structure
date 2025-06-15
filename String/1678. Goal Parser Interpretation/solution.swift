class Solution {
    func interpret(_ command: String) -> String {
        
        var ans : String = ""
        
        var i : Int = 0
        
        while i < command.count {
                        
            if i+4 <= command.count {
                
                let start = command.index(command.startIndex, offsetBy: i)
                let end = command.index(command.startIndex, offsetBy: i+4)
                
                if command[start..<end] == "(al)" {
                    ans += "al"
                    i+=4
                    continue
                }
            }
            
            if i + 1 < command.count {
                
                if command[command.index(command.startIndex, offsetBy: i)] == "(", command[command.index(command.startIndex, offsetBy: i+1)] == ")" {
                    
                    ans += "o"
                    i+=2
                    continue
                }
                
           }
            
            if command[command.index(command.startIndex, offsetBy: i)] == "G" {
                ans += "G"
                i+=1
            }
            
        }
        
        return ans
    }
}

// Example 1:
let command = "G()(al)"
print(Solution().interpret(command))

// Example 2:
let command = "G()()()()(al)"
print(Solution().interpret(command))


// Example 3:
let command = "(al)G(al)()()G"
print(Solution().interpret(command))
