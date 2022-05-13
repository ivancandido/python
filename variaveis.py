nome="Ivan Candido"
empresa = 'Itau'
qtde_funcionarios = 500
mediamensalidade = 856.50
idade = int(input("Informe sua idade: "))

print(nome)
print(empresa)
print("Possui ", qtde_funcionarios, " funcionarios.")
print("média mensalidade " + str(mediamensalidade))

if idade >= 50:
    print("Idade maior que 50")
    print("passou no maior que 50")
else:
    print("Idade menor que 50")
    print("passou no menor que 50")
