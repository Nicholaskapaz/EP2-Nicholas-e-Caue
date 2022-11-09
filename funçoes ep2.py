# Transforma base de questoes
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


# Valida uma questao
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