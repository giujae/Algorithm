def solution(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append("(")
        elif bracket == ")":
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True