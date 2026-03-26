# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

senha = 2002
i = True
while i:
    tentativa = int(input("Antes de tudo, digite sua senha: "))
    if tentativa == senha:
        print("senha correta, seja bem vindo !!")
        i = False
    else:
        print("senha incorreta, tente novamente")