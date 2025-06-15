class Solution {
    func subtractProductAndSum(_ n: Int) -> Int {
        
        
        var product : Int = 1
        var totalSum : Int = 0
        
        for x in String(n){
            
            if let x = Int(String(x)) {
                product *= x
                totalSum += x
            }
        }
        
        
        return product - totalSum
    }
}



let n = 234
print(Solution().subtractProductAndSum(n))