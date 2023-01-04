c = float(input('Qual a temperatura em °C'))
f = 32
k = 273.15
conv = (c*9/5)+f
conv1 = c+k
print(f'{c}°C, equivale à {conv:.1f}°F \nE a {conv1:.1f}°K')
ff = float(input('Qual a temperatura em °F'))
print(f'{ff}°F, equivalem á {(ff-32)*5/9:.1f}°C \n e á {(ff-32)*5/9+273.15:.1f}°k')
