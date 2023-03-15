# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
# is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.\
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def daily_temperatures(temperatures: list[int]) -> list[int]:
    output = [0] * len(temperatures)
    i = 0
    stack = []
    while i < len(temperatures) - 2:
        if temperatures[i+1] <= temperatures[i]:
            stack.append(i)
        else:
            output[i] = 1
        i = i+1
    
    while stack:
        a = stack.pop()
        while stack and temperatures[a] <= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            output[stack[-1]] = a - stack[-1]
    return output

print(daily_temperatures([1, 3,2,1,3]))