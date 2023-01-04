tpa = int(input('Diga o termo da PA: '))
rpa = int(input('Agora a razão: '))
a = 10
pa = 0
pa = pa + tpa
while a > 0:
    a -= 1
    print(f'{pa} >', end=' ')
    pa += rpa
    if a == 0:
        qq = str(input('\ndeseja continuar mostrando a sequência? [sim/não] ')).lower()
        if qq == 'sim':
            a = 1
            a = int(input('Quantas sequências deseja: '))
            while a > 1:
                a -= 1
                print(f'{pa} >', end=' ')
                pa += rpa
        else:
            print("FIM")
