def inverter(palavra:str)->str :
    return palavra[::-1]

#--------------------------------

def inverter_exemplo(texto):
    contrario = ""
    for letra in texto:
        contrario = letra + contrario
    return contrario
print(inverter_exemplo('Ingride'))
#-------------------------------------
# Cria uma variavel vazia chamada CONTRARIO, crio um for para percorrer o texto usando a variavel LETRA, substituo o conteudo da variavel CONTRARIO por LETRA + CONTRARIO(q é a variavel vazia). Essa ordem acaba influenciando na ordem de que o for vai armazenar os caracteres na variavel CONTRARIO, já que o for itera um caracter por vez
#----------------------------------
#Inverter string - Fatiamento

    #return palavra[0:len(texto):-1]
    #range (inicio, fim e passo)
    

#------------------------------------

def contar(texto:str):
    