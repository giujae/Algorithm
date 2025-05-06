class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        result = [0] * n # 정답을 저장 할 배열
        stack = [] # index를 넣을 스택

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]: # 현재 온도가 stack의 최상단 index의 온도보다 높을 때
                prev_idx = stack.pop()
                result[prev_idx] = idx - prev_idx # 순회하는 동안 현재 온도가 더 높은 경우들의 경과 일 수를 기록
            stack.append(idx) # 온도가 더 낮다면 스택에 넣음
        
        return result
        