from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()

        suggestions = []

        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            result = []
            for pr in products:
                if pr.startswith(prefix):
                   result.append(pr)
                if len(result) == 3:
                    break
            suggestions.append(result)
        
        return suggestions


if __name__ == '__main__':

    """ Example 1: """
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    print(Solution().suggestedProducts(products, searchWord))