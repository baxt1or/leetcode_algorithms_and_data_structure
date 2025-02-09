import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        letters = list(string.ascii_lowercase)

        key = self.remove(key.replace(" ", ""))

        vocabulary = {key[i]:letters[i] for i in range(len(key))}

        message = list(message)

        for i in range(len(message)):
            if message[i] in vocabulary.keys():
                message[i] = vocabulary[message[i]]
        return "".join(message)


    
    def remove(self, message):
        ans = ''
        seen = []

        for c in message:
            if c not in seen:
                ans+=c
                seen.append(c)
        return ans
        

if __name__ == "__main__":
    
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(Solution().decodeMessage(key, message))