class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {')' : '(', ']' : '[', '}' : '{'}

        for string in s:
            if string in brackets.values():
                stack.append(string)
            elif string in brackets:
                if not stack or stack[-1] != brackets[string]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack
