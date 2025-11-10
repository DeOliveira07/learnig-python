#inciando estruturas condicionais

#tempo de vida de um carro

# idade_carro = int(input('digite quantos anos tem o seu carro'))


# if(idade_carro<=3):
#     print('seu carro é novo')
# else:
#     print('seu carro não é novo')



# nome_pesso = str(input('digite seu nome: '))
# nome_pessoa_dif = str(input('digite o nome da outra pessoa: '))

# if(nome_pesso == nome_pessoa_dif):
#     print('estamos falando da mesma pessoa')


# else:
#     print(f'por {nome_pesso} ser diferente de {nome_pessoa_dif}, entramos no else ')

# nota_um = float(input('digite a primeira nota : '))
# nota_dois = float(input('digite a segunda nota : '))
# media = (nota_um + nota_dois)/2
# print(f'a sua média foi {media:.1f}')

# if(media>=7):
#     print('por isso você passou')

# else:
#     print('por isso você não passou')


#hora dos desafios 

#28 gerar um numero alatório até 5 e descobrir
# from random import randint

# aleatorio = randint(0,5)
# escolha = int(input('escolha um numero: '))

# if escolha == aleatorio:
#     print('voce escolheu o numero certo')

# else:
#     print('escolheu o numero errado')

# print(aleatorio)

#29 sistema de multa

# km = int (input ('digite quantos km você andou '))
# hr = int (input('digite quantos tempo em horas você andou '))
# velocidade = km/hr  #velocidade em km/h
# vel_max = 80

# if (velocidade > vel_max):
#     ultrapassagem = velocidade - vel_max
#     multa = ultrapassagem * 7
#     print(f'por ter ultrapassado em  {ultrapassagem} km/h o limite de {vel_max} km/h , você pagará uma multa de {multa} reais')

# else:
#     print('não foi multado')


#30 (par ou impar)

# num = int (input('digite um numero '))
# if(num%2==0):
#     print('par')

# else:
#     print('impar')

# desafio 31(taxa de viagem)

# a partir de de 200km a taxa diminui

# deslocamento = int(input('quantos km vc se deslocou?'))

# if(deslocamento <= 200 ):
#     print(deslocamento*0.5)

# else:
#     print(deslocamento*0.45)


#32 desafio do ano bissexto 
# while(True):
#     ano = int(input('digite um ano: '))

#     if(ano%4==0 and ano % 100 != 0 ) or (ano % 400 == 0):

#         print(' bissexto')

#     else:
#         print('não bissexto')
#         break


# 33(maior,menor)

# a =  int(input('digite um número: '))
# b =  int(input('digite um número: '))
# c =  int(input('digite um número: '))

# maior=''
# menor=''

# if(a>b and a>c):
#     maior = a
#     if(b>c):
#         menor = c
#     elif(c>b):
#         menor = b

# if(b>a and b>c):
#     maior = b
#     if(a>c):
#         menor = c
#     elif(c>a):
#         menor = a 

# if(c>a and c>b):
#     maior = c
#     if(a>b):
#         menor = b
#     elif(b>a):
#         menor = a


# print(f'o maior número é {maior}')
# print(f'o menor número é {menor}')


#34 (aumento de salário )

#para salarios superiores a 1250 , aumento de 10%
#para salarios inferiores a 1250 , aumento de 15%

# salario = float(input('digite seu salario '))
# base = 1250.0

# if(salario > base):
#     calc = salario + ((10/100)*salario)
#     print(f'seu salario teve um aumento de 10% e passou a ser {calc}')

# else:
#     calc = salario + ((15/100)*salario)
#     print(f'seu salario teve um aumento de 15% e passou a ser {calc}')

#35 (condição de formação de triangulos)


# 33(maior,menor)

# a =  int(input('digite um número: '))
# b =  int(input('digite um número: '))
# c =  int(input('digite um número: '))

# maior=''
# menor=''
# meio =''

# if(a>=b and a>=c):
#     maior = a
#     if(b>c):
#         menor = c
#         meio = b
#     elif(c>b):
#         menor = b
#         meio = c
#     else:
#         menor = b
#         meio = c

# if(b>=a and b>=c):
#     maior = b
#     if(a>c):
#         menor = c
#         meio = a 
#     elif(c>a):
#         menor = a
#         meio = c
#     else:
#         menor = a
#         meio = c

# if(c>=a and c>=b):
#     maior = c
#     if(a>b):
#         menor = b
#         meio = a
#     elif(b>a):
#         menor = a
#         meio = b
#     else:
#         menor = a
#         meio = b



# print(f'o maior número é {maior}')
# print(f'número do meio é {meio}')
# print(f'o menor número é {menor}')

# print('o calculo depende que o maior lado seja menor que a soma dos outros dois')
# tri = meio + menor

# if(maior < tri):
#     print(' triangulo aceito')

# else:
#     print(f'triangulo nn pode ser criado pois , a soma entre {meio} e {menor} resulta em {tri} e isso é menor que {maior}')



