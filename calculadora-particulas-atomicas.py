# encoding: utf-8
# Criado em: Quarta-feira 27/Fev/2019 hs 11:29
# Autor: olverclock


titulo = 'Cáuculadora das partículas atômicas'
print('-' * 50)
print(titulo.center(50))
print('-' * 50)
a = int(input('Digite a massa do seu átomo: '))
z = int(input('Digite o número atómico : '))
print('-' * 68)
print('Rápida explicação: eletróns tem carga (negativa) e próton (positiva)')
print('Então o Átomo que Perde eletróns é chamado de Pátion e é positivo')
print('E um Átomo que ganha eletróns é chamado de Ânion e é negativo')
print('-' * 68)
p = z
e = z
sim = 'SIM'
nao = 'NÃO'
n = a - p
x = z - 1
sn = str(input('Seu átomo é eletricamente neutro?(SIM OU NÃO) !  '))
if sn == sim:
 print('#'*88,'\n')
 print('Respondeu SIM então os eléntrons é igual a número de protóns E = Z seu número de elétrons é :) Então E =',e)
 print('O número de protóns é igual ao número atômico P = Z! :) Então P =', p)
 print('O número de nêutrons é Massa igual a protóns mais nêutrons A=P+N ! :) Então N =', n)
else:
 if sn == nao:
    numero = int(input('Repondeu NÂO então qual valor da carga? :'))
      if numero > 0:
      print('#'*78,'\n')
      print('Esse valor corresponde que o átomo está positivo pois perdeu elétrons, valor é :) Então E =', z - numero)
      print('O número de protóns é igual ao número atômico P = Z! :) Então P =', p)
      print('O número de nêutrons é Massa igual a protóns mais nêutrons A=P+N ! :) Então N =', n)
    else:
      if numero < 0:
       print('#'*78,'\n')
       print('Esse valor corresponde que o átomo está negativo pois ganhou elétrons, valor é :) Então E =',z - numero)
       print('O número de protóns é igual ao número atômico P = Z! :) Então P =', p)
       print('O número de nêutrons é Massa igual a protóns mais nêutrons A=P+N ! :) Então N =', n)

fim = input('Aperte qualquer tecla para fechar:')