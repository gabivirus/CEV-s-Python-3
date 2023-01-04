list = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > list[-1]:
        list.append(n)
    else:
        p = 0
        while p < len(list):
            if n <= list[p]:
                list.insert(p, n)
                break
            p += 1

print('O valor em ordem é: ', list)


'''
for c in range(5):
    n = int(input('Digite um número: '))
    list.append(n)
    for i, v in enumerate(list):
        print('.')
        if len(list) == 1:
            list.append(n)
        else:
            if list[i+1] >= n:
                list.insert(i, n)
            elif n > list[-1]:
                list.append(n)

print('O valor em ordem é: ', list)'''
