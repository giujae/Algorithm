def solution(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append("(")
        elif bracket == ")":
            try:
                stack.pop()
            except IndexError:
                return False
    if stack:
        return False
    else:
        return True