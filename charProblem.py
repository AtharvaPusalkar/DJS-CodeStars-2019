def commonChar(s):
    charCount = {}
    for i in s:
        if i not in s:
            charCount[i] = s.count(i)
    maxChar = ''
    maxCount = 0
    for j in charCount.keys():
        if charCount[j] > maxCount:
            maxChar = j
            maxCount = charCount[j]
        elif charCount[j] == maxCount and j < maxChar:
            maxChar = j
    return maxChar