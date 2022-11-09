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
