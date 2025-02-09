class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        keyboard = {ch:i for i, ch in enumerate(keyboard)}

        ans = []
        position = 0

        for i in range(len(word)):
            if word[i] in keyboard.keys():
                index = keyboard[word[i]]
                ans.append(abs(index - position))
                position = index
        return sum(ans)
    
if __name__ == "__main__":

    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    print(Solution().calculateTime(keyboard, word))