print('Pense em um número de 0 - 10 e eu irei descobri-lo através de algumas perguntas mas peço que as responda somente com "sim" ou "não" ')
pronto = input ('Já  pensou? Se estiver pronto para começar pressione a tecla "ENTER". ')

p1 = input('O número é maior ou igual a 5? ').lower()
if p1 == "sim":

    p2 = input('Seu número é par? ').lower()
    if p2  == "sim":  
       p3 = input('O número é maior ou igual a 8? ').lower()
       if p3 == "sim":
           p4 = input('O número é maior que 9? ').lower()
           if p4 == "sim":  
               print('Aaah descobri rapaz, seu número é o 10!!  ')
           elif p4 == "não" or "nao":
                  print('Aaah descobri rapaz, seu número é o 8!!  ')
           else: 
                  print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
       elif p3 == "não" or "nao":
          print('Aaah descobri rapaz, seu número é o 6!!  ') 
       else:
           print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
    elif p2 == "não" or "nao": 
        p6 = input('O número é maior ou igual a 7? ').lower()
        if p6 == "sim":
            p7 = input('O número é maior 8? ').lower()
            if p7 == "sim":
                print('Aaah descobri rapaz, seu número é o 9!! ')
            elif p7 == "não" or "nao": 
                p8 = input('O número é maior 6? ').lower() 
                if p8 == "sim":
                    print('Aaah descobri rapaz, seu número é o 7!! ')  
                elif p8 == "não" or "nao": 
                    print('Aaah descobri rapaz, seu número é o 5!! ')
                else:
                    print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
            else:
                print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
        elif p6 == "não" or "nao":
            print('Aaah esse foi muito fácil rapaz, seu número é o 5!! Faça alugum outro mais difícil. ')
        else:
                print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
    else:
                print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 

                
elif p1 == "não" or "nao":
    p9 = input('Seu número é par? ').lower()
    if p9  == "sim":  
       p10 = input('O número é maior ou igual a 2? ').lower()
       if p10 == "sim":
           p11 = input('O número é maior que 3? ').lower()
           if p11 == "sim":  
               print('Aaah descobri rapaz, seu número é o 4!!  ')
           elif p11 == "não" or "nao":
                  print('Aaah descobri rapaz, seu número é o 2!!  ') 
       elif p10 == "não" or "nao":
          print('Aaah descobri rapaz, seu número é o 0!!  ') 
       else:
           print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
    elif p9 == "não" or "nao": 
        p13 = input('O número é maior que 2? ').lower()
        if p13 == "sim":
            print('Aaah descobri rapaz, seu número é o 3!! ')
        elif p13 == "não" or "nao": 
            print('Aaah descobri rapaz, seu número é o 1!! ')  
        else:
            print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
    else:
            print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 
else: 
    print('Ei cara, é necessário saber escrever "sim" e "não" para participar desta "brincadeira", aprenda e volte para jogar novamente. ') 