# manipulando textos

texto = 'curso em videO' #coube em 1 espaço de memória porem a cadeia de caracteres tem um numero maior

#fatiamento 
print(texto[9]) #toda string é um vetor de char por isso eu consigo localizar a letra 9
print(texto[9:13]) #começa no 9 e exclui o 12 , 1 a menos no final
print(len(texto))
print(texto.count('o')) # CASE SESITIVY DO 
print(texto.find('deO'))
print(texto.find('look')) # se a string não existe o meu retorno com o find é o -1
print ('curso' in texto)
print(texto.replace('curso','python')) #primeiro argumento é o que eu vou trocar , o segundo é pelo o que eu vou trocar