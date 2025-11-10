# # ordem de Precedencia em um calculo

# # () -> parêntese 01
# # ** -> potência 02
# # * -> mult, /-> divisão, // -> divisão inteira , % ->mod  03
# # + -> soma , - -> subtração  04

# resultado_um = 5+2*3 # se for exectado dessa forma o primeiro a ser resolvido é a mult(2*3), 6+5 = 117      

# print(resultado_um)

# resultado_dois = 3*5+4**2

# print(resultado_dois)

# #em python temos 2 tipos de divião , uma inteira e outra real, irei usar o mesmo numerador e denominador

# tipo_um = 9//2
# tipo_dois = 9/2

# print(f'tipo 1 com o // não tem valor quebrado {tipo_um} , já o tipo dois com / faz o reultado se comportar com um float {tipo_dois}')

# # indo mais além, brincando com raiz e potência

# # o ** é utilizado para fazer uma potencia porem, uma melhor forma de manipular se chama pow

# a = 3
# b = 4

# print('pow(3,4) tem o resultado de 3 elevado a 4 ',pow(3,4))

# #raiz indiretamente é o inverso da potencia

# print('81**(1/2)',81**(1/2)) #irá calcular a raiz quadrada

# #brincando com algumas funcionalidades do print
# aa='aaaaaaaaaaaaaaaaaa'
# print(f'o numero escolhido foi {aa:=^20} ')

# #ex5 (sucessor e antecessor)

# num = int(input('numero: '))
# sucessor = num+1
# antecessor = num-1

# print(f' do numero {num}, o sucessor é : {sucessor} e o antecessor é o {antecessor}')

# #ex6 dobro,triplo e raiz
# dobro = num*2
# triplo = dobro*1.5
# raiz= num**(1/2) #o inverso da potencia é justamente a raiz

# print(f'dobro: {dobro}, triplo: {triplo}, raiz: {raiz}')

# #ex7 media entre duas nota

# nome = str(input('digite seu nome: '))
# nota_um = float(input('digite a primeira nota: '))
# nota_dois = float(input('digite a segunda nota: '))

# media = (nota_um+nota_dois)/2

# print(f'olá {nome}, sua média será {media}')# teste: 9+10 = 19/2 8.5

# #ex8 conversão em unidade de medidas(centimetro,milimetro,kilometro) recebendo do usuário o valor em metros

# metros = int(input('digite quantos metros vc quer converter'))
# cent=metros*100 #1 metro tem 100 centimetros
# mili = metros * 100 # 1 metro tem 1.000 milimetros
# km = metros/1000 # 1km tem 1.000 metros logo km tem metros/1.000

# print(f'com a conversão de {metros} metros , temos {cent} centimetros, {mili} mili e por fim {km} km')


# #já conhecia um pouco sobre estruturas de repetição , vou fazer por ela

# # irei receber o mesmo num que usei no dobro , triplo e raiz

# for tabuada in range(1,11):
#     print(f'{num} x {tabuada} = {num*tabuada}')

# # print(tabuada)

# #ex11 (area da parede e quantidade de lata de tintas)

# largura = float(input('digite a largura da sua parede '))
# altura  = float(input('digite a altura da sua parede '))

# area_quad = largura * altura

# quant_tinta = area_quad/2

# print(f'com a area de : {area_quad} m2 , precisaremos de {quant_tinta} litros de tinta')#1 l de tinta pinta 2m2   se eu tiver 4m2 precisarei de 2l de tinta logo para saber o l de tinta area / 2

# #ex13 aumento de salario de func

# salario_func = float(input('digite seu salario '))
# aumento_percet = 15/100
# aumento_percet_errado = 115/100
# novo_salario = salario_func + (salario_func * aumento_percet) 
# novo_salario_errado = salario_func * aumento_percet_errado # testando com 100, o resultado será 115

# print(novo_salario)#sem a utilização do round o resultado estava saindo um pouco aproximado
# print(novo_salario_errado)

#ex 15 , aluguel de carros ,dia e km rodado

dias = int(input('quantos dias vc passou com o carro ')) #3 dias
km = float(input('quantos km vc rodou ')) #350 km

diaria = dias * 60 
km_rodado = km * 0.15 

tot = diaria + km_rodado

print(tot) 

