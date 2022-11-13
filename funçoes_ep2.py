import random

# 1. Transforma base de questoes
def transforma_base(base_de_questoes):
    dicionario = {}
    for lista in base_de_questoes:
        n = lista['nivel'] #n recebe a lista com o value da key 'nível' (no caso, "facil")
        if n not in dicionario:
            dicionario[n] = []  #assim eu adiciono uma key (no caso "facil", que eu quero que seja apresentada na saída como uma key) no dicionário
        dicionario[n].append(lista) #com o append eu adiciono um dicionário na lista. Na key fácil, eu quero adicionar um dicionário
    return dicionario

    # lista = {
    #     'titulo': 'Qual o resultado da operação 57 + 32',
    #     'nivel': 'facil',
    #     'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    #     'correta': 'C'
    # }


# 2. Valida uma questao
def valida_questao(questao):
    dicionario = {}
    tem_titulo = False
    tem_nivel = False
    tem_opcoes = False
    tem_correta = False
    tem_outro = False
    for chaves in questao.keys():
        if chaves == 'titulo':
            tem_titulo = True
        elif chaves == 'nivel':
            tem_nivel = True
        elif chaves == 'opcoes':
            tem_opcoes = True
        elif chaves == 'correta':
            tem_correta = True
        # else:
        #     tem_outro = True
        
    if tem_titulo != True: #se o tem_titulo tem True, então eu sei que ele tem o título escrito certo
        dicionario['titulo'] = 'nao_encontrado'
    if tem_nivel != True:
        dicionario['nivel'] = 'nao_encontrado'
    if tem_opcoes != True:
        dicionario['opcoes'] = 'nao_encontrado'
    if tem_correta != True:
        dicionario['correta'] = 'nao_encontrado'

 #   if tem_titulo == False or tem_nivel == False or tem_opcoes == False or tem_correta == False or tem_outro == True:
    if len(questao) != 4:
        dicionario['outro'] = 'numero_chaves_invalido'

    if tem_titulo == True:
        if questao['titulo'].strip() == '': #o strip tira os espaços em excesso
            dicionario['titulo'] = 'vazio'

    if tem_nivel == True:
        if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
            dicionario['nivel'] = 'valor_errado'

    if tem_opcoes == True:
        if len(questao['opcoes']) != 4:
            dicionario['opcoes'] = 'tamanho_invalido'
        else:
            achou = False
            for chaves2 in questao['opcoes']:
                if chaves2 != 'A' and chaves2 != 'B' and chaves2 != 'C' and chaves2 != 'D':
                    dicionario['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                    achou = True

            if achou == False:
                dic_op = {}
                if questao['opcoes']['A'].strip() == '':
                    dic_op['A'] = 'vazia'
                    dicionario['opcoes'] = dic_op

                if questao['opcoes']['B'].strip() == '':
                    dic_op['B'] = 'vazia'
                    dicionario['opcoes'] = dic_op

                if questao['opcoes']['C'].strip() == '':
                    dic_op['C'] = 'vazia'
                    dicionario['opcoes'] = dic_op

                if questao['opcoes']['D'].strip() == '':
                    dic_op['D'] = 'vazia'
                    dicionario['opcoes'] = dic_op
            
    if tem_correta == True:
        if questao['correta'] != 'A' and questao['correta'] != 'B'and questao['correta'] != 'C' and questao['correta'] != 'D':
            dicionario['correta'] = 'valor_errado'

    return dicionario

        # chaves = {
        #       'titulo': 'Qual o resultado da operação 57 + 32?',
        #     'nivel': 'facil',
        #     'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
        #     'correta': 'C'

        # }


# 3. Valida Lista de Questões
def valida_questoes(lista_de_questoes):
    lista = []

    for questao in lista_de_questoes:
        dic = valida_questao(questao)
        lista.append(dic)
    return lista


# 4. Sorteia Uma Questão
def sorteia_questao(dic2, nivel2):
    sorteio = random.randint(0, len(dic2[nivel2])-1)
    return dic2[nivel2][sorteio]
    #eu começo na posição 0, pegando o len do dicionário, se tiver 20 questões, a última está na posição 19. Se eu coloco de zero a vinte e
    #ele sorteia a questão vinte, vai dar erro pq a minha última questão está na posiçaõ 19.

# 5. Sorteia uma Questão Inédita
def sorteia_questao_inedita(dic3, nivel3, questoes_ja_sorteadas):
    questao2 = sorteia_questao(dic3, nivel3)     
    while questao2 in questoes_ja_sorteadas:
        questao2 = sorteia_questao(dic3, nivel3)
    questoes_ja_sorteadas.append(questao2)
    return questao2



# 6. Questao para testo 
def questao_para_texto(dic_questao, numero_questao):
    texto = '----------------------------------------\n'
    texto += 'QUESTAO ' + str(numero_questao) + '\n'
    texto += ' \n'
    texto +=  dic_questao['titulo'] + '\n'
    texto += ' \n'
    texto += 'RESPOSTAS:\n'
    texto += 'A: ' + dic_questao['opcoes']['A'] + '\n'
    texto += 'B: ' + dic_questao['opcoes']['B'] + '\n'
    texto += 'C: ' + dic_questao['opcoes']['C'] + '\n'
    texto += 'D: ' + dic_questao['opcoes']['D'] + '\n'
    return texto


# 7. Gera Ajuda em uma Questão!

def gera_ajuda(dic2_questao):
    if 'A' == dic2_questao['correta']:
        quest_correta = 0
    elif 'B' == dic2_questao['correta']:
        quest_correta = 1
    elif 'C' == dic2_questao['correta']:
        quest_correta = 2
    elif 'D' == dic2_questao['correta']:
        quest_correta = 3
    quantas_sortear = random.randint(1, 2)
    l = ['A', 'B', 'C', 'D']

    i = 0
    x = True
    achou_primeira = False
    sorteada = -1  #-1 pq é um número diferente dos q ele pode sortear
    while i < quantas_sortear:
        quest_sorteada = random.randint(0, len(dic2_questao['opcoes'])-1)
        if quest_sorteada == quest_correta or quest_sorteada == sorteada:
            x = True
        elif achou_primeira == False:
            sorteada = quest_sorteada
            achou_primeira = True
            x = False
            texto2 = 'DICA:\n'
            texto2 += 'Opções certamente erradas: '
            texto2 += dic2_questao['opcoes'][l[quest_sorteada]]
            i += 1
        else:
            texto2 += ' | ' + dic2_questao['opcoes'][l[quest_sorteada]] 
            i += 1
    #texto2 += "'"
    return texto2


