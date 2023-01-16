list = []

for c in range(0, 5):
    n = int(input('Digite um número: '))
    print(n, list)
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
