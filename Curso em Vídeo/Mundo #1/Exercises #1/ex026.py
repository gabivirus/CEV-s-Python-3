nome = str(input('Digite uma frase: ')).strip().lower()
n = nome.count('a')
f = nome.find('a')+1
s = nome.rfind('a')+1

print(f'''tem {n} "a´s" na sua frase
o primeiro "a", está na posição: {f}
e o último na: {s}''')
