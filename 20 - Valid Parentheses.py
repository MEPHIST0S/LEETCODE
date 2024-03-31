#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:
    #Open brackets must be closed by the same type of brackets.
    #Open brackets must be closed in the correct order.
    #Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(seld, s):
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or \
                    (i == ')' and stack[-1] != '(') or \
                    (i == '}' and stack[-1] != '{') or \
                    (i == ']' and stack[-1] != '['):
                    return False 
                stack.pop() 
        return not stack  

# Example of Usage!
solution = Solution()
s = "{[()()]}"
print(solution.isValid(s))
                    