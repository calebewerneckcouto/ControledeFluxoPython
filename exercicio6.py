'''Um número primo é um número que é divisível apenas por 1 e por ele mesmo.
Escreva um programa que receba um número n e informe se esse número é primo
ou não.'''



n = int(input("Informe um número: "))


if n <= 1:
    print(f"{n} não é um número primo.")
else:
   
    eh_primo = True

    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            eh_primo = False
            break

   
    if eh_primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")
