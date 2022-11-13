import lib_questoes
import funçoes_ep2

lista = []

print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n\n')
nome = input('Qual seu nome? ')
print('Ok ' + nome + ' você tem direito a pular 3 vezes e 2 ajudas!\n')
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
input('Aperte ENTER para continuar... ')


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