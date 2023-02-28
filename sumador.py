variable1 = 1
variable2 = 2
variable3 = 3
variable4 = 4

print(f"{variable1},{variable2},{variable3},{variable4}")

lista_variables = [variable1, variable2, variable3, variable4]
for posicion in range(len(lista_variables)):
    print(lista_variables[posicion])

print(f"{lista_variables[0] + lista_variables[1] + lista_variables[2] + lista_variables[3]}")