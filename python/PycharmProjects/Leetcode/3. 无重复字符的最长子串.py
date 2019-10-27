class Solution:
    def isValid(self, s: str) -> bool:
        dict ={'(':')','[':']','{':'}'}
        current = 0
        stack = []
        while (current < s.__len__()):
            if (s[current] == '(' or s[current] == '[' or s[current] == '{'):
                stack += s[current]
            elif(s[current] == ')' or s[current] == ']' or s[current] == '}'):
                if (stack.__len__()>0 and dict[stack[stack.__len__()-1]]==s[current]):
                    del stack[stack.__len__()-1]
                else:
                    return 0
            current += 1
        if (stack.__len__()):
            return 0
        else:
            return 1

class __main__:
    s='()'
    solu = Solution()
    b=solu.isValid(s)
    print(b)