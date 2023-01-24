studentsGrade = {}


def grade(* value, confirm = 'no'):
    studentsGrade['quantidade de notas'] = len(value)
    studentsGrade['maior'] = max(value)
    studentsGrade['menor'] = min(value)
    studentsGrade['média'] = sum(value)/len(value)

    if confirm in 'yesim':
        if studentsGrade['média'] >= 5:
            studentsGrade['situação'] = 'aprovado'

        else:
            studentsGrade['situação'] = 'reprovado'
    
    return studentsGrade


grade(6, 0, 10, confirm = 'yes')

print('-='*30)
for value, key in enumerate(studentsGrade):
    print(f'A {key} é: {value}')

print('-='*30)

