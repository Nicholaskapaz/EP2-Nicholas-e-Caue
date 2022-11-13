import lib_questoes
import funçoes_ep2

lista = []

print('\33[35mOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n\n')
nome = input('\33[mQual seu nome? ')
print('Ok ' + nome + ' você tem direito a pular 3 vezes e 2 ajudas!\n')
print('\33[36mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
input('\33[mAperte ENTER para continuar... ')


lista = funçoes_ep2.valida_questoes(lib_questoes.quest)
for q in lista:
    if len(q) > 0:
        print('Inconsistência na base de perguntas. O Programa será encerrado')
        exit()

print('O jogo já vai começar! Lá vem a primeira questão!')
print('Vamos começar com questões do nível FACIL!')
input('Aperte ENTER para continuar... ')



questoes_ja_sorteadas = []
dic_questoes = {}
dic_questoes = funçoes_ep2.transforma_base(lib_questoes.quest)
premio = ['1000', '5000', '10000', '30000', '50000', '100000', '300000', '500000']
qtd_ajuda = 2
qtd_pulo = 3
val_premio = '0'
quer_parar = ['S', 'N']
lista2 = ['A', 'B', 'C', 'D', 'AJUDA', 'PULA', 'PARAR']
i = 0
acertou = True

while i < 9:
    if acertou == True:
        if i <= 2:
            questoes = funçoes_ep2.sorteia_questao_inedita(dic_questoes, 'facil', questoes_ja_sorteadas)
        elif i >= 3 and i <= 5:
            questoes = funçoes_ep2.sorteia_questao_inedita(dic_questoes, 'medio', questoes_ja_sorteadas)
        else:
            questoes = funçoes_ep2.sorteia_questao_inedita(dic_questoes, 'dificil', questoes_ja_sorteadas)
        questoes2 = funçoes_ep2.questao_para_texto(questoes, i+1)
        pediu_ajuda = False
    print(questoes2)

    resposta = input('Qual sua resposta?! ').upper()
    if resposta not in lista2:
        print('Opção inválida!\n')
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
        acertou = False
    else:
        if resposta == 'AJUDA':
            if qtd_ajuda == 0:
                print('Não deu! Você não tem mais direito a ajuda!')
                input('Aperte ENTER para continuar... ')
                acertou = False
            elif qtd_ajuda == 2:
                pediu_ajuda = True
                qtd_ajuda -= 1
                print('Ok, lá vem ajuda! Você ainda tem 1 ajuda!\n\n')
                input('Aperte ENTER para continuar... ')
                ajuda = funçoes_ep2.gera_ajuda(questoes)
                print(ajuda)
                acertou = False
            elif qtd_ajuda == 1:
                if pediu_ajuda == True:
                    print('Não deu! Você já pediu ajuda nesta questão!\n')
                    input('Aperte ENTER para continuar... ')
                    acertou = False
                else:
                    qtd_ajuda -= 1
                    print('Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!\n')
                    input('Aperte ENTER para continuar... ')
                    ajuda = funçoes_ep2.gera_ajuda(questoes)
                    print(ajuda)
                    acertou = False
        elif resposta == 'PULA':
            if qtd_pulo == 0:
                print('Não deu! Você não tem mais direito a pulos!\n')
                input('Aperte ENTER para continuar... ')
                acertou = False
            elif qtd_pulo == 3:
                qtd_pulo -= 1
                print('Ok, pulando! Você ainda tem 2 pulos!\n')
                input('Aperte ENTER para continuar... ')
                acertou = True
            elif qtd_pulo == 2:
                qtd_pulo -= 1
                print('Ok, pulando! Você ainda tem 1 pulo!\n')
                input('Aperte ENTER para continuar... ')
                acertou = True
            else:
                qtd_pulo -= 1
                print('Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!\n')
                input('Aperte ENTER para continuar... ')
                acertou = True