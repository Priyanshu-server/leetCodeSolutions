class Solution(object):
    def func(self,strs):
        if not strs:
            return ""
        shortest_string  = min(strs)

        for indx,char in enumerate(shortest_string):
            for string in strs:
                if string[indx] != char:
                    return "" if indx == 0 else string[:indx]

        return shortest_string



sol = Solution()
print(sol.func(['flower','flwe','flrw']))
