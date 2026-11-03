salario_atual = float(input('Informe o salário: '))
percentual = float (input ('Informe o digito para percentual: '))

percentual = percentual / 100

aumento = salario_atual * percentual
novo_salario = salario_atual + aumento 

print (f'\nSalario anterior: {salario_atual}')
print (f'Reajuste de: {aumento}')
print (f'Novo salário: {novo_salario}')





