class Solution(object):
    def generateParenthesis(self, n):
        result = []
        self.generate("",n, n,result)
        return result

    def generate(self,string,open_br,close_br,result):
        if open_br>close_br or open_br<0 or close_br<0:
            return 
        if open_br == 0 and close_br == 0:
            result.append(string)
        self.generate(string+"(", open_br-1, close_br, result)
        self.generate(string+")", open_br, close_br-1, result)
        
sol = Solution()
print(sol.generateParenthesis(3))