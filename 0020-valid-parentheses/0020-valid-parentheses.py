class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {')' : '(', ']' : '[', '}' : '{'}

        for string in s:
            if string in brackets.values(): # 열려있는 괄호일 경우 스택에 넣는다
                stack.append(string)
            elif string in brackets: # 닫혀있는 괄호일 경우
                if not stack or stack[-1] != brackets[string]: # 스택이 비었거나 스택의 가장 위 원소가 짝이 맞지 않는 다면 거짓
                    return False
                stack.pop() # 거짓이 아니라면 스택에서 제거
            else:
                return False # brackets가 아닐 경우 거짓
        
        return not stack # for문이 모두 순회 한 후 남아있는 게 있다면(짝이 맞지 않는다는 것) 거짓, 비어있다면 참
