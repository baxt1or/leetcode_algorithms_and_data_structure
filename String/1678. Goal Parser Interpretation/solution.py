class Solution:
    def interpret(self, command: str) -> str:
                
        answer = ''

        i = 0
        
        while i < len(command):
            if command[i] == 'G':
                answer += 'G'
                i+=1
            elif command[i] == '(' and command[i+1] == ')':
                answer += 'o'
                i+=2 
            elif command[i] == '(' and command[i:i+4] != ')':
                answer += 'al'
                i+=4 
                
        return answer

if __name__ == '__main__':

    """ Example 1: """
    command = "G()(al)"
    print(Solution().interpret(command=command))

    """ Example 2: """
    command = "G()()()()(al)"
    print(Solution().interpret(command=command))

    """ Example 3: """
    command = "(al)G(al)()()G"
    print(Solution().interpret(command=command))