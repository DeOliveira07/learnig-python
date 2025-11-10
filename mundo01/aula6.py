#tipos primitivos e utilização correta do input

n1 = int(input('digite um numero ')) # a variável irá receber um tipo inteiro
n2 = float(input('digite um numero quebrado ')) #a variavel irá receber um numero quebrado , ex:15.123
n3=bool(input('é verdade ou não? '))#irá receber o argumento booleano, verdadeiro ou falsof

print(n1,n2,n3)

#guanabara usou o format mas a já existe o f string

print(f'o valor n1 recebe {n1} , a variável n2 {n2} , o n3 será {n3}')

#testando os tipos utilizand a validação com booleano

n4 = input('digite algo ')
print(n4.isnumeric())