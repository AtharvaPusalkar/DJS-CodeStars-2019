def commonK(t):
    for i in range(t):
        n = int(input())
        a_list = list(map(int, input().rstrip().split()))
        p_list = list(map(int, input().rstrip().split()))
        q_list = list(map(int, input().rstrip().split()))
        addition = []
        for j in p_list:
            addition.extend(range(j+1))
        subtraction = []
        for k in q_list:
            subtraction.extend(range(k+1))
        operations = []
        for l in range(len(a_list)):
            for m in addition:
                operations.extend(a_list[l]-m)
            for n in subtraction:
                operations.extend(a_list[l]-n)
        n_eq = []
        for p in operations:
            if p==n:
                n_eq.append(p)
        print(len(n_eq))

t = int(input())

commonK(t)