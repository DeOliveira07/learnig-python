#primeiros coimandos em python 3

# escrever números sem valores numéricos referencialos com aspas
# o número com valor numerico não precisa de aspas

a=7
b="7"
print(a,b)
print('o valor de a é ',type(a))
print('o valor de v é ',type(b))

#recebendo valores e imprimindo na tela
#utilizar o comando input
print('----------------------------------------')
nome=input('qual é o seu nome? ')
idade=int(input('qual a sua idadede?'))
print('nome: ',nome)
print('idade',idade)
print('----------------------------------------')
#desafio 1(nome e mensagem de boas vindas)

nome_pessoa = input('qual o seu nome ?')
print('----------------------------------------')
print('seja-bem vindo ao nosso establecimento ',nome_pessoa)

#desafio 2 ( mês,ano e dia e formatar a data)

dia_nascimento = int(input('digite a data de nascimento '))
mes_nascimento = int(input('digite o mes de nascimento '))
ano_nascimento = int(input('digite o ano de nascimento '))
print('olá ', nome_pessoa,' seja bem-vindo')
print('vc nasceu nesta data',dia_nascimento,'/',mes_nascimento,'/',ano_nascimento)

#desafio 3 (soma entre 2 numeros)

num_pri = int(input('digite um numero '))
num_sec = int(input('digite um numero '))
soma= num_pri + num_sec
print(soma) 

