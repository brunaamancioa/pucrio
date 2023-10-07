primeiroNumero = float (input ('Digite o primeiro número: '))
segundoNumero = float (input('Digite o segundo número:  ')) 
                      
print("1. Adição (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")
operador = input('Digite o número da operação que deseja realizar:  ')

if operador == '1':
    print("O resultado da soma é {} ".format(primeiroNumero + segundoNumero))
elif operador == '2':
    print("O resultado da subtração é {} ".format(primeiroNumero - segundoNumero))
elif operador == '3':
    print("O resultado da multiplicação é {} ".format(primeiroNumero * segundoNumero))
elif operador == '4':
    print("O resultado da soma é {} ".format(primeiroNumero / segundoNumero))