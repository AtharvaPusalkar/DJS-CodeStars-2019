def maxChar(s):
    maxChar = ''
    maxCount = 0
    for i in s:
        if s.count(i) > maxCount:
            maxChar = i
            maxCount = s.count(i)
        elif s.count(i) == maxCount and i < maxChar:
            maxChar = i
    return maxChar

string = str(input())
maxChar(string)
