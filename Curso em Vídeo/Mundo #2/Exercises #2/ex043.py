print('IMC')
mt = int(input('Digite sua altura em centímetros: '))
ps = float(input('Agora seu peso: '))
x = ps/(mt*mt)*10000
if x < 18.5:
    print(f'\033[34mAbaixo do peso\033[m\nseu \033[34mIMC\033[m é de \033[34m{x:.4}\033[m')
elif x < 25 > 18.4:
    print(f'\033[32mPeso ideal\033[m\nseu \033[32mIMC\033[m é de \033[32m{x:.4}\033[m')
elif x < 30 > 24.9:
    print(f'\033[33mSobrepeso\033[m\nseu\033[m \033[33mIMC\033[m é de \033[33m{x:.4}\033[m')
elif x < 40 > 29.9:
    print(f'\033[31mObesidade\033[m\nseu \033[31mIMC\033[m é de \033[31m{x:.4}\033[m')
elif x > 39.9:
    print(f'\033[33;41mObesidade morbida\033[m\nseu \033[33;41mIMC\033[m é de \033[33;41m{x:.4}\033[m')