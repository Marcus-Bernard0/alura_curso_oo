#planos: descobrir uma maneira de colocar níveis, variando as tentativas
#planos: dar dica sobre palavras

import random


def jogar():
    print("\n")
    print("*************************************")
    print("Bem vindo ao jogo da forca")
    print("*************************************")

    arquives = open("palavra.txt", "r")
    palavra = []

    for linha in arquives:
      linha = linha.strip()
      palavra.append(linha)

     
    #text = arquives.read()
    #print(text)
    
    arquives.close()
    

   
    numero_aleatorio = random.randrange(0, len(palavra))
    
    
    palavra_secreta = palavra[numero_aleatorio].upper()

    #estando implementação de dicas, estudar uma forma com funções para não usar if
    palavra_secreta = palavra[numero_aleatorio].upper()
    letras_corretas = ["_" for letras in palavra_secreta] #list comprehension.
    #for letras in palavra_secreta: Outra maneira de fazer.
        #letras.append("_")
    
    enforcou = False
    acertou  = False
   
    erros = 0
    tentativas = len(palavra_secreta) - 4 #tentativas de acordo com a palavra.
    
    print("\n")
    print(f"Se errar {tentativas} vezes. Já era! ")
    print("\n")

    print("Quando acertar, o jogo irá mostrar a letra que você chutou.")
    print(f'Dica: A palavra secreta tem {len(palavra_secreta)}, {letras_corretas} letras.')

    #for teste in palavra:
    if numero_aleatorio == 2:
        print("Comida de sabado")
    
    elif numero_aleatorio == 1:
        print("Tela")
    
    while (not enforcou and not acertou):
        
        chute = input("Insira sua letra: ")
        chute = chute.strip().upper() #retira os espaços em brancos
        
        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                    if (chute == letra): 
                        #print(f"Parabéns encontrou a letra {letra} na posição {posicao}")
                        letras_corretas [posicao] = letra
                    posicao +=1 
               
        else:
            erros +=1
        
        acertou = "_" not in letras_corretas
        enforcou = erros == tentativas     
        print(letras_corretas)
    

    if acertou:
        print("Boa, continue .")
    else: 
        print(f"Que pena, a palvra era {palavra_secreta}")

        print("Fim do game")

if (__name__== "__main__"):
    jogar()