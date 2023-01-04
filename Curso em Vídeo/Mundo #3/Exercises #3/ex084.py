count = mai = men = 0
ppl = []
namep = []
namel = []
rppl = list()


print('='*30, 'Cadastro de pesagem', '='*30)
while True:
    prs = str(input('Digite um nome: '))
    wgt = int(input('Insira um peso: '))
    ppl.append(prs)
    ppl.append(wgt)
    rppl.append(ppl[:])

    if count == 0:
        mai = men = wgt
        namep.append(prs)
        namel.append(prs)
    else:
        if wgt > mai:
            namep.clear()
            mai = wgt
            namep.append(prs)
        elif wgt == mai:
            mai = wgt
            namep.append(prs)

        elif wgt < men:
            namel.clear()
            men = wgt
            namel.append(prs)
        elif wgt == men:
            men = wgt
            namel.append(prs)

    count += 1

    q = input('Deseja continuar cadastrando? ')
    if q in 'NOPNONNAONÃOnopnonnaonão':
        break

print(f'\n\033[1;34mForam registradas {count} pessoas.\033[m')

print(f'\nA(s) pessoa(s) mais com maior peso fora: ', end='\033[31m')
for c in namep:
    print(c, end=', ')

print(f'\n\n\033[mE (as) pessoa(s) mais com menor peso fora: ', end='\033[32m')
for c in namel:
    print(c, end=', ')
print('\n\033[m')
