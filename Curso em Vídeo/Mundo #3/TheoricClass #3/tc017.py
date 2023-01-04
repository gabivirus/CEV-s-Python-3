num = [2, 5, 9, 8, 7, 3, 1]

num[2] = 3

num.append(4)

#num.sort(reverse=True)

#num.insert(2, 0)

#num.pop()
#num.pop(0)

if num.count(7) > 1:
    num.remove(1)

print(num)
print(f'Essa lista tem {len(num)} elementos')