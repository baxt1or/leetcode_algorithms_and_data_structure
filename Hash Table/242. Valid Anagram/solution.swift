class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool  {
        
        let s_count = self.get_frequency(s: s)
        let t_count = self.get_frequency(s: t)
        
        return s_count == t_count
    }
    
    func get_frequency(s:String) -> [Character:Int] {
        
        var frequency : [Character: Int] = [:]
        
        for c in Array(s){
            frequency[c, default : 0] += 1
        }
        
        return frequency
    }
}



let s = "anagram"
let t = "nagaram"
print(Solution().isAnagram(s, t))