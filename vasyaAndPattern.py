def vasyaAndPattern(n):
    for i in range(n+1, 0):
        output = ''
        for i in range(1, n+1):
            output += str(i)
        print(output)
        print('\n')

number = int(input())
vasyaAndPattern(number)
