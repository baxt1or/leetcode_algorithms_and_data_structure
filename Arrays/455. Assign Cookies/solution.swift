class Solution {
    func findContentChildren(_ g: [Int], _ s: [Int]) -> Int {
        
        let g : [Int] = g.sorted()
        let s: [Int] = s.sorted()

        var child : Int = 0
        var cookie : Int = 0

        while child < g.count && cookie < s.count {

            if s[cookie] >= g[child]{
                child+=1
            }

            cookie+=1
        }

        return child

    }
}