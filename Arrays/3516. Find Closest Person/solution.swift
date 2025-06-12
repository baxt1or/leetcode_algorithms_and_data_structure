class Solution {
    func findClosest(_ x: Int, _ y: Int, _ z: Int) -> Int {
        
        let first : Int = abs(z-x)
        let second : Int = abs(z - y)
        
        if first < second {
            return 1
        } else if first  == second {
            return 0
        } else {
            return 2
        }
    }
}


let x :Int = 2
let y :Int = 7
let z : Int = 4

print(Solution().findClosest(x, y, z))