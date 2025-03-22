class Solution {
    func isValid(_ word: String) -> Bool {
        
        let vowels = Set(Array("aeiouAEIOU"))
        let uppercaseLetters = (65...90).map { Character(UnicodeScalar($0)!) }
        let lowercaseLetters = (97...122).map { Character(UnicodeScalar($0)!) }

        let consonants = Set(uppercaseLetters + lowercaseLetters).subtracting(vowels)
        
        let digits = Set(Array("0123456789"))
        
        var has_consonants = false
        var has_vowels = false
        
        if word.count < 3 {
            return false
        }
        
        
        for char in Array(word){
            
            if vowels.contains(char){
                has_vowels = true
            }
            else if consonants.contains(char){
                has_consonants = true
            }
            else if !digits.contains(char){
                return false
            }
        }
        
        return has_vowels && has_consonants
    }
}

let word = "234Adas"
print(Solution().isValid(word))