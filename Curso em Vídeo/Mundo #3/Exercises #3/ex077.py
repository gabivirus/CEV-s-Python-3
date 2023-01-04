vog = ('a', 'e', 'i', 'o', 'u')
pal = ('Matuto', 'Render', 'Upar', 'Deletar', 'Defusar', 'Thayna', 'Vera', 'Nayara')

for p in pal:
    print(f'\nNa palavra {p}', end=' ')
    for c in p:
        if c.lower() in 'aeiou':
            print(c.lower(), end=' ')
