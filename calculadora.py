 # essa e uma calculadora 100% open source feita por mim :)
def soma(x, y): #define operação soma
    return x + y

def menos(x, y):#define operação subitração
    return x - y

def multiplica(x, y):#define operação multiplicação
    return x * y

def divide(x, y):#define operação divisão
    return x / y
print ("Selecione uma operação")#apresentação do programa
print ("1- Soma")
print ("2- Subtração")
print ("3- multiplicação")
print ("4- divisão")

escolha = input("Opção:")#faz a variavel de escolha

numero1 = int(input("Escolha primeiro numero:"))#numero 1   
numero2 = int(input("Escolha segundo numero:"))#numero 2

if escolha == '1':
        print(numero1,"+",numero2,"=", soma(numero1,numero2))
elif escolha == '2':
        print(numero1,"-",numero2,"=", menos(numero1,numero2))
elif escolha == '3':
        print(numero1,"*",numero2,"=", multiplica(numero1,numero2))
elif escolha == '4':
        print(numero1,"/",numero2,"=", divide(numero1,numero2))
else:
        print("Input invalido")#Faz as contas com as variaveis 