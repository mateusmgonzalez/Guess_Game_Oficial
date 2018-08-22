from tkinter import*
from random import*



## funções
def verificaEntrada(palpite):
    """
    Retorna um booleano dizendo se a entrada é válida
    ou não, tendo em vista o número de dígitos
    True --> Entrada Válida
    False --> Entrada Inválida
    """
    if palpite < 1 or palpite >= 100:
        return False
    else:
        return True
def tentativa(palpite):
    """
    Função verifica a entrada do usuário
    """
    global jogada, alvo
    palpite = palp.get()
    try:
        palpite = int(palpite)
        lista.append(palpite)
    except ValueError:
        msg['text'] = 'Entrada Invalida\n Digite apenas números!'
        msg['fg'] = 'red'
        return
    if not verificaEntrada(palpite):
        msg['text'] = 'Digite números entre 0 e 100!'
        msg['fg'] = 'red'
    else:
        jogada += 1
        dicas = GeraDicas(palpite,alvo)
            
        jgds['text'] = '%i/10'%jogada
        if palpite == alvo:
            botao['state'] = DISABLED
            msg['text'] = "Ganhou"
            dica1['text'] = ""
            dica2['text'] = ""

        if jogada == 10 :
            #E nós colocamos a mensagem de derrota
            perdeu()
    palp.delete (0, END)
 
def GeraDicas(palpite, alvo):
      """
      Recebe o número escolhido e o número secreto
      
      """
      global lista, jogada 
      if jogada == 1:    
            if (abs(alvo - palpite) <= 3 and alvo != palpite):
                  dica1['text'] = "Muito quente"
            elif (abs(alvo - palpite) >= 4 and abs(alvo - palpite) <= 6):
                  dica1['text'] = "Quente"
            elif (abs(alvo - palpite) >= 7 and abs(alvo - palpite) <= 10 ):
                  dica1['text'] = "Frio"
            elif (abs(alvo - palpite) > 10):
                  dica1['text'] = "Muito Frio"
             
      if jogada > 1:

            distancia_anterior = abs(alvo - lista[jogada - 2])
            distancia_atual = abs(alvo - lista[jogada -1])
            #o anterior está Fervendo
            if (distancia_anterior <= 3 and alvo != palpite):
                  if (distancia_atual <= 3):
                       dica1['text'] = "Seu palpite continua muito quente"
                  elif (distancia_atual >= 4 and distancia_atual <= 6 and alvo != palpite):
                        dica1['text'] = "OOps, seu palpite deu uma esfriada mas ainda está quente"
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        dica1['text'] = "OOps, seu palpite agora ficou frio!"
                  else :
                        dica1['text'] = "OOps, seu palpite agora ficou muito frio!"
            #o anterior é muito quente
            if (distancia_anterior <= 3 and alvo != palpite):
                  if (distancia_atual <= 3):
                        dica1['text'] = "Seu palpite continua muito quente"
                  elif (distancia_atual >= 4 and distancia_atual <= 6 and alvo != palpite):
                        dica1['text'] = "OOps, seu palpite deu uma esfriada mas ainda está quente"
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        dica1['text'] = "OOps, seu palpite agora ficou frio!"
                  else :
                        dica1['text'] = "OOps, seu palpite agora ficou muito frio!"
            
            #anterior é quente           
            elif (distancia_anterior >= 4 and distancia_anterior <= 6 and alvo != palpite):
                  if(distancia_atual<= 3):
                        dica1['text'] = "OOps, seu palpite deu uma esquentada e agora está muito quente!"
                  elif (distancia_atual >= 4 and distancia_atual <= 6):
                        if (distancia_anterior > distancia_atual):
                              dica1['text'] = "Teu palpite está se aproximando mais continua quente!"
                        else:
                              dica1['text'] = "Seu palpite acabou se afastando, mas continua quente!"
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        dica1['text'] = "OOps, seu palpite deu uma esfriada e agora ficou frio!"
                  else :
                        dica1['text'] = "OOps, seu palpite agora ficou muito frio!"
             #o anterior é morno
            if (distancia_anterior <= 3 and alvo != palpite):
                  if (distancia_atual <= 3):
                        dica1['text'] = "Seu palpite continua muito quente"
                  elif (distancia_atual >= 4 and distancia_atual <= 6 and alvo != palpite):
                        dica1['text'] = "OOps, seu palpite deu uma esfriada mas ainda está quente"
                  elif(distancia_atual >= 7 and distancia_atual <= 10):
                        dica1['text'] = "OOps, seu palpite agora ficou frio!"
                  else :
                        dica1['text'] = "OOps, seu palpite agora ficou muito frio!"
            #anterior é frio
            elif (distancia_anterior >= 7 and distancia_anterior <= 10 and alvo != palpite):
                  if(distancia_atual<= 3):
                        dica1['text'] = "OOps, seu palpite deu uma esquentada e agora está muito quente!"
                  elif (distancia_atual >= 4 and distancia_atual <= 6):
                        dica1['text'] = "Seu palpite deu uma esquentada e agora está quente!"
                  elif(distancia_atual >= 7 and distancia_atual <= 10 ):
                        if (distancia_anterior > distancia_atual):
                              dica1['text'] = "Teu palpite está se aproximando mais continua frio!"
                        else:
                              dica1['text'] = "Seu palpite acabou se afastando, mas continua frio!"
                        
                  else :
                        dica1['text'] = "OOps, seu palpite deu uma esfriada e agora ficou muito frio!"
            #anterior é muito frio
            elif (distancia_anterior > 10 and alvo != palpite):
                  if(distancia_atual <= 3):
                        dica1['text'] = "OOps, seu palpite deu uma esquentada e agora está muito quente!"
                  elif (distancia_atual >= 4 and distancia_atual <= 6):
                        dica1['text'] = "Seu palpite deu uma esquentada e agora está quente!"
                  elif(distancia_atual >= 7 and distancia_atual <= 10 ):
                        dica1['text'] = "OOps, seu palpite deu uma esquentadinha mas ainda está frio!"
                  else :
                        if (distancia_anterior > distancia_atual):
                              dica1['text'] = "Teu palpite está se aproximando mais continua muito frio!"
                        else:
                             dica1['text'] = "Seu palpite acabou se afastando, mas continua muito frio!"
            if (distancia_anterior < distancia_atual):
                   dica2['text'] = "Está se aproximando"
            else:
                   dica2['text'] = "Agora se afastou"


def perdeu():
      global alvo
      botao['state'] = DISABLED
      msg['text'] = "Perdeu"
      msg['text'] = 'O numero era %i' %alvo
## Propriedades do jogo

i = Tk()
i.geometry("400x300")
i.title("Guess_Game")

## Botões e texto
palp = Entry(i,text ="" )
palp.pack()
botao = Button(i, text = "Arriscar",command = lambda: tentativa(palp) )
botao.pack()
dica1 = Label(i, text ='Digite um numero de 1 a 100')
dica1.pack()
dica2 = Label(i, text ='Tente acertar')
dica2.pack()
jgds = Label(i, text ='0/10')
jgds.pack()

msg = Label(i,text = 'GuessGame')
msg.pack()



# variaveis
# conta quantas jogadas o usuário já fez
jogada = 0
#armazenará as jogadas do usuário
lista = []
# numero secreto
alvo = randint(1,100)


i.mainloop()
