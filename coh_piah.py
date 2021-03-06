import re

def __main__():
    ass = le_assinatura()
    textos = le_textos()
    print("O autor do texto ",avalia_textos(textos,ass)," está infectado com COH-PIAH")

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e ndevolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    
    data = frase.split(",")
    string = str(data).strip('[]')
    s = ""
    for i in string:
      if i not in (",","'"):
        s = s+i
    
    
    return s.split()
  

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    cont = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma_a = 0
    soma_b = 0
    for i in as_a:
        soma_a = soma_a+i
    for i in as_b:
        soma_b = soma_b+i
   
    if soma_a >= soma_b:     
        ass = (soma_a - soma_b)/6
    else:
        ass= (soma_b - soma_a)/6
        
    return ass

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    
    dados = []
    dados.append(tamanho_medio_palavras(texto))
    dados.append(type_token(texto))
    dados.append(rh_legomana(texto))
    dados.append(tamanho_medio_sentenca(texto))
    dados.append(complexidade_sentenca(texto))
    dados.append(tamanho_medio_frase(texto))
    return dados
    
def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = len(textos) -1
    tex = 0
    lista = []
    while tex <= i:
        a = calcula_assinatura(textos[tex])
        lista.append(compara_assinatura(a,ass_cp))
        tex += 1
    
    tex = 1
    for item in lista:
        if item == min(lista):
            return tex
        else:
            tex +=1  


def tamanho_medio_palavras(texto):
   '''Essa função recebe um texto e devolve o tamanho medio de palavras'''
    letras = 0
    
    frases = string(separa_frases(string(separa_sentencas(texto))))
    p = separa_palavras(frases)
    for i in p:
        for n in i:
            if n not in (' '):
                letras += 1
                
    print(len(p), letras)
    media = letras/len(p)

    return media
    
def type_token(texto):
    ''' Essa funçao recebe um texto e devolve Type_Token do texto'''

    frases = string(separa_frases(string(separa_sentencas(texto))))
    palavras = 0
    palavras_diferentes = n_palavras_diferentes(separa_palavras(frases))
    
    
    for i in separa_palavras(frases):
        
        palavras += 1
        
    
    media = palavras_diferentes/palavras
    
    return media

def rh_legomana(texto):
    ''' Essa funçao recebe um texto e devolve RH Legomana do texto'''

    frases = string(separa_frases(string(separa_sentencas(texto))))
    palavras = 0
    palavras_unicas = n_palavras_unicas(separa_palavras(frases))
    
    for i in separa_palavras(frases):
        palavras += 1
    
    media = palavras_unicas/palavras
    
    return media

def tamanho_medio_sentenca(texto):   
    ''' Essa funçao recebe um texto e devolve o tamanho medio de sentença do texto'''
    caracteres = 0
    sentencas = 0
    
    for i in separa_sentencas(texto):
        
        sentencas += 1
        for n in i:
            if n not in (".","!","?"):
                caracteres+=1
                
            else:
                continue;
            
    media = caracteres/sentencas
    
    return media
 
def complexidade_sentenca(texto):
    ''' Essa funçao recebe um texto e devolve a complexidade de sentença do texto'''

    sentencas = str(separa_sentencas(texto)).strip('[]')
    numero_frases = len(separa_frases(sentencas))
    numero_sentencas = len(separa_sentencas(texto))
    
    
    media = numero_frases/numero_sentencas
    
    
    return media

def tamanho_medio_frase(texto):
    ''' Essa funçao recebe um texto e devolve o tamanho medio de frase do texto'''
    
    letras = 0
    sentencas = str(separa_sentencas(texto)).strip('[]')
    numero_frases = len(separa_frases(sentencas))
    for i in separa_frases(texto):
        for n in i:
            if n not in (",",".","!","?"):
                
                letras += 1
        
    media = letras/numero_frases
    
    return media

def string(func):

    s = ""
    for i in func:
        if i not in ("'"," "):
            s = s+" "+i
        
        
        
        
    return s.strip("[]")
    
