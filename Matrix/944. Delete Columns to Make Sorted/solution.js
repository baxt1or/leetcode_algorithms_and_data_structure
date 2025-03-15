var minDeletionSize = function(strs) {
    
    let count = 0

    for(let c =0;c< strs[0].length;c++){
        
        let row = []

        for(let word of strs){
            row.push(word[c])
        }

        word = row.join('')
        word_sorted = row.sort().join('')

        if(word != word_sorted){
            count++
        }
        
    }

    return count
};



const strs = ["cba","daf","ghi"]
console.log(minDeletionSize(strs))