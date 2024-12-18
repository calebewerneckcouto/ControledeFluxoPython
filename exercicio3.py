'''Escreva um programa de autenticação que receba um nome de usuário e senha
( input ) informe se:
Exercícios – Controle de Fluxo 2
Autenticação foi bem-sucedida.
Se o nome de usuário não existe.
Se a senha está incorreta.
Os valores corretos de nome de usuário e senha devem estar armazenados em
constantes, como no exemplo abaixo:
USUARIO = "admin"
SENHA = "123123"
nome_usuario = input("Digite o nome do usuário: "\n)
'''

'''Considerar usuario admin  e senha  123123'''

nome_usuario = input("Digite o nome do usuário: ")
senha=input("Digite senha do usuário: ")

if nome_usuario != "admin":
    print("nome de usuário não existe")
elif senha != "123123":
    print("senha está incorreta")  
else:
    print("Autenticação foi bem-sucedida")      



