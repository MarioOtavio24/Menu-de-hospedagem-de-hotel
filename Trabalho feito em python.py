
import os
os.system ('cls')
#Aqui está o menu, aonde o usúario pode visualizar suas opções de apartamento, pessoas, e tipos.
try:
    orçamento=int (input ('''
    Apartamento para uma pessoa(1)
    Diária tipo 1 R$ 20,00  
    Diária tipo 2 R$ 25,00
 
    Apartamento para duas pessoas(2)
    Diária tipo 1 R$28,00
    Diária tipo 2 R$34,00
 
    Apartamento para três pessoas(3)
    Diária tipo 1 R$35,00
    Diária tipo 2 R$42,00
 
    Apartamento para quatro pessoas(4)
    Diária tipo 1 R$42,00
    Diária tipo 2 R$50,00
 
    Apartamento para cinco pessoas(5)
    Diária tipo 1 R$48,00
    Diária tipo 2 R$ 57,00
 
    Apartamento para seis pessoas(6)
    Diária tipo 1 R$53,00
    Diária tipo 2 R$63,00
    
    ==> Digite a quantidade de pessoas no apartamento '''))
except ValueError:
     print('Só é permitido valor númerico de 1 a 6 e tipos 1 e 2')

if orçamento>6 or orçamento<1:
    print('número invalido')

else:

    diariatipos=int(input('qual tipo você deseja? '))

    if diariatipos==(1) and orçamento==1: # Do lado esquerdo fica o tipo do apartamento, do lado direito fica a quantidade de pessoas.
        print('diária de R$20,00')
    elif diariatipos==(2) and orçamento==1:
        print('diária de R$25,00')
    elif diariatipos==(1) and orçamento==2:
        print('diária de R$28,00')
    elif diariatipos==(2) and orçamento==2:
        print('diária de R$34,00')
    elif diariatipos==(1) and orçamento==3:
        print('diária de R$35,00')
    elif diariatipos==(2) and orçamento==3:
        print('diária de R$42,00')
    elif diariatipos==(1) and orçamento==4:
        print('diária de R$42,00')
    elif diariatipos==(2) and orçamento==4:
        print('diária de R$50,00')
    elif diariatipos==(1) and orçamento==5:
        print('diária de R$48,00')
    elif diariatipos==(2) and orçamento==5:
        print('diária de R$57,00')
    elif diariatipos==(1) and orçamento==6:
        print('diária de R$53,00')
    elif diariatipos==(2) and orçamento==6:
        print('diária de R$63,00')
    print('você acabou de confirmar a sua estadia.')

