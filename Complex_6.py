import cmath
num_complexo_str = input("Digite o primeiro número complexo a+bj no formato (a, b): ")
num_complexo_str = num_complexo_str.replace('(', '').replace(')', '')
partes = num_complexo_str.split(',')

if len(partes) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real = float(partes[0])
    parte_imaginaria = float(partes[1])
num_complexo_str2 = input("Digite o primeiro número complexo a+bj no formato (a, b): ")
num_complexo_str2 = num_complexo_str2.replace('(', '').replace(')', '')
partes2 = num_complexo_str2.split(',')

if len(partes2) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real2 = float(partes2[0])
    parte_imaginaria2 = float(partes2[1])
z1 = complex(parte_real,parte_imaginaria)
z2 = complex(parte_real2,parte_imaginaria2)

print("|c1||c2|=|c1c2|:\t", (abs(z1) * abs(z2) == abs(z1 * z2)))
print("|c1+c2| <= |c1| + |c2|:\t", (abs(z1 + z2) <= abs(z1) + abs(z2)))
