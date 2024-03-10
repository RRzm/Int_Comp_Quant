import cmath
num_complexo_str = input("Digite o primeiro número complexo a+bj no formato (a, b): ")
num_complexo_str = num_complexo_str.replace('(', '').replace(')', '')
partes = num_complexo_str.split(',')

if len(partes) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real = float(partes[0])
    parte_imaginaria = float(partes[1])
num_complexo_str2 = input("Digite o segundo número complexo a+bj no formato (a, b): ")
num_complexo_str2 = num_complexo_str2.replace('(', '').replace(')', '')
partes2 = num_complexo_str2.split(',')

if len(partes2) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real2 = float(partes2[0])
    parte_imaginaria2 = float(partes2[1])
num_complexo_str3 = input("Digite o terceiro número complexo a+bj no formato (a, b): ")
num_complexo_str3 = num_complexo_str3.replace('(', '').replace(')', '')
partes3 = num_complexo_str3.split(',')

if len(partes3) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real3 = float(partes3[0])
    parte_imaginaria3 = float(partes3[1])
z1 = complex(parte_real,parte_imaginaria)
z2 = complex(parte_real2,parte_imaginaria2)
z3 = complex(parte_real3,parte_imaginaria3)

print("Comutativa:")
print("c1 + c2 = c2 + c1\t",(z1 + z2 == z2 + z1))
print("c1*c2 = c2*c1\t", (z1*z2==z2*z1))
print("Associativa:")
print("(c1+c2)+c3=c1+(c2+c3)\t",((z1 + z2)+z3 == z1 +(z2 + z3)))
print("(c1*c2)*c3=c1*(c2*c3)\t",((z1 * z2)*z3 == z1 *(z2 * z3)))
print("Distributividade:")
print("c1*(c2+c3) = c1*c2+c1*c3\t",(z1*(z2+z3)==z1*z2 + z1*z3))

