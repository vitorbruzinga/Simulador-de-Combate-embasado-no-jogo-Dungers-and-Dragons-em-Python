# Importação da biblioteca padrao Json

import json
import sys

#------------------------------------

# declarações de sys.argv para receber parametros na linha de comando
char1 = sys.argv[1]
char2 = sys.argv[2]
#--------------------------------------------------------------------

# importando bases de dados para simulador///Inicio
with open("armor.json", "r", encoding="utf8") as arm:
    armadura = json.load(arm)

with open("attributes.json", "r", encoding="utf8") as at:
    attributes = json.load(at)

with open("weapons.json", "r", encoding="utf8") as wp:
    armas = json.load(wp)

with open(char1, "r", encoding="utf8") as c1:
    personagem1 = json.load(c1)

with open(char2, "r", encoding="utf8") as c2:
    personagem2 = json.load(c2)
# -----------------------------------------------------FIm

# Função de rodar dados, de acordo com numero de lados//Inicio
def dado(x):
    import random
    x = random.randint(1, x)
    return x
# --------------------------------------------------------Fim /

# Indicador de turnos dos personagens
turno1 = (f'Turno do personagem {personagem1["name"]}')
turno2 = (f'Turno do personagem  {personagem2["name"]}')
# -------------------------------------------------------

# declaração de atributos extraidos da base de dados
hp_personagem1 = personagem1["HP"]
forca_personagem1 = personagem1["strength"]
destreza_personagem1 = personagem1["dexterity"]
atack_personagem1 = dado(20) + forca_personagem1
new_class_armor1 = 0
new_class_armor2 = 0
hp_personagem2 = personagem2["HP"]
forca_personagem2 = personagem2["strength"]
destreza_personagem2 = personagem2["dexterity"]
atack_personagem2 = dado(20) + float(forca_personagem2)
# ------------------------------------------------------

# Declaração de classes de armadura iniciais
armadura_1 = personagem1['armor']
armadura_2 = personagem2['armor']
type_armor1 = armadura[armadura_1]['type']
type_armor2 = armadura[armadura_2]['type']
class_armor1 = armadura[armadura_1]['AC']
class_armor2 = armadura[armadura_2]['AC']
# -----------------------------------------------------

# Declaração de armas iniciais
arma_1 = personagem1['weapon']
arma_2 = personagem2['weapon']
damage_1 = armas[arma_1]['damage']
damage_2 = armas[arma_2]['damage']
props_1 = armas[arma_1]['props']
props_2 = armas[arma_2]['props']
# -----------------------------------------------------

# Regra de Classe de armadura para personagem 1
if(props_1 == 'finesse' and personagem1["shield"] == 'true'):
    new_class_armor1 = 2

if(type_armor1 == 'light'):
    new_class_armor1 += class_armor1 + destreza_personagem1

elif(type_armor1 == 'medium' and personagem1["dexterity"] >= 2):
    new_class_armor1 += class_armor1 + 2

elif(type_armor1 == 'heavy'):
    new_class_armor1 += class_armor1
# ---------------------------------------------------------------------------------#

#  Regra de Classe de armadura para personagem 2
if(props_2 == 'finesse' and personagem2["shield"] == 'true'):
    new_class_armor2 = 2

if(type_armor2 == 'light'):
    new_class_armor2 += class_armor2 + destreza_personagem2

elif(type_armor2 == 'medium' and personagem1["dexterity"] >= 2):
    new_class_armor2 += class_armor2 + 2

elif(type_armor2 == 'heavy'):
    new_class_armor2 += class_armor2
# ----------------------------------------------------------------------------------

# função para o personagem 1 atacar o personagem 2///Inicio
def ataque1vs2(hp_personagem2):
    print('\n\n', turno1)
    atack_personagem1 = dado(20) + forca_personagem1

    if(personagem1["dexterity"] > personagem1["strength"] and props_1 == 'finesse'):
        atack_personagem1 = dado(20) + destreza_personagem1

    if(atack_personagem1 > new_class_armor2):
        print('O ataque acertou')
        print('Classe de armadura do alvo: ', new_class_armor2)
        print('Rolando dados para calculo do dano: ')

        if(damage_1 == 'd4'):
            dano_personagem1 = dado(4) + forca_personagem1
            hp_personagem2 = hp_personagem2 - dano_personagem1
            print('Resultado da rolagem de dano: ', dano_personagem1)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
            print('Total de pontos de vida restante do alvo: ', hp_personagem2)
            
            if(props_1 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))

                if(alternativa == 1):
                    dano_personagem1 = dado(4) + destreza_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-destreza_personagem1, '\nBonus de forca: ', destreza_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

                else:
                    dano_personagem1 = dado(4) + forca_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

        elif(damage_1 == 'd6'):
            dano_personagem1 = dado(6) + forca_personagem1
            hp_personagem2 = hp_personagem2 - dano_personagem1
            print('Resultado da rolagem de dano: ', dano_personagem1)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
            print('Total de pontos de vida restante do alvo: ', hp_personagem2)
           
            if(props_1 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))

           
                if(alternativa == 1):
                    dano_personagem1 = dado(6) + destreza_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-destreza_personagem1, '\nBonus de forca: ', destreza_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

                else:
                    dano_personagem1 = dado(6) + forca_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

        elif(damage_1 == 'd8'):
            dano_personagem1 = dado(8) + forca_personagem1
            hp_personagem2 = hp_personagem2 - dano_personagem1
            print('Resultado da rolagem de dano: ', dano_personagem1)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
            print('Total de pontos de vida restante do alvo: ', hp_personagem2)
           
            if(props_1 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))

                if(alternativa == 1):
                    dano_personagem1 = dado(8) + destreza_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-destreza_personagem1, '\nBonus de forca: ', destreza_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

                else:
                    dano_personagem1 = dado(8) + forca_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                         hp_personagem2)

        elif(damage_1 == 'd10'):
            dano_personagem1 = dado(10) + forca_personagem1
            hp_personagem2 = hp_personagem2 - dano_personagem1
            print('Resultado da rolagem de dano: ', dano_personagem1)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
            print('Total de pontos de vida restante do alvo: ', hp_personagem2)

            if(props_1 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))

                if(alternativa == 1):
                    dano_personagem1 = dado(10) + destreza_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-destreza_personagem1, '\nBonus de forca: ', destreza_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

                else:
                    dano_personagem1 = dado(10) + forca_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

        elif(damage_1 == 'd12'):
            dano_personagem1 = dado(12) + forca_personagem1
            hp_personagem2 = hp_personagem2 - dano_personagem1
            print('Resultado da rolagem de dano: ', dano_personagem1)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
            print('Total de pontos de vida restante do alvo: ', hp_personagem2)
            
            if(props_1 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))

                if(alternativa == 1):
                    dano_personagem1 = dado(12) + destreza_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-destreza_personagem1, '\nBonus de forca: ', destreza_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

                else:
                    dano_personagem1 = dado(12) + forca_personagem1
                    hp_personagem2 = hp_personagem2 - dano_personagem1
                    print('Resultado da rolagem de dano: ', dano_personagem1)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem1-forca_personagem1, '\nBonus de forca: ', forca_personagem1)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem2)

        else:
            print('Erro inesperado, reinicie o programa. ')
            return
    else:
        print('O ataque nao acertou')
    return hp_personagem2
# ----------------------------------------------------------------------------------------Fim /

# função para o personagem 2 atacar o personagem 1///Inicio
def ataque2vs1(hp_personagem1):
    print('\n\n', turno2)
    atack_personagem2 = dado(20) + forca_personagem2
    
    if(personagem2["dexterity"] > personagem2["strength"] and props_2 == 'finesse'):
        atack_personagem2 = dado(20) + destreza_personagem2
    
    if(atack_personagem2 > new_class_armor1):
        print('O ataque acertou')
        print('Classe de armadura do alvo: ', new_class_armor1)
        print('Rolando dados para calculo do dano: ')

        if(damage_2 == 'd4'):
            dano_personagem2 = dado(4) + forca_personagem2
            hp_personagem1 = hp_personagem1 - dano_personagem2
            print('Resultado da rolagem de dano: ', dano_personagem2)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
            print('Total de pontos de vida restante do alvo: ', hp_personagem1)
           
            if(props_2 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))
           
                if(alternativa == 1):
                    dano_personagem2 = dado(4) + destreza_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-destreza_personagem2, '\nBonus de forca: ', destreza_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)
               
                else:
                    dano_personagem2 = dado(4) + forca_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)

        elif(damage_2 == 'd6'):
            dano_personagem2 = dado(6) + forca_personagem2
            hp_personagem1 = hp_personagem1 - dano_personagem2
            print('Resultado da rolagem de dano: ', dano_personagem2)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
            print('Total de pontos de vida restante do alvo: ', hp_personagem1)
            
            if(props_2 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))
                
                if(alternativa == 1):
                    dano_personagem2 = dado(6) + destreza_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-destreza_personagem2, '\nBonus de forca: ', destreza_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)
               
                else:
                    dano_personagem2 = dado(6) + forca_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)

        elif(damage_2 == 'd8'):
            dano_personagem2 = dado(8) + forca_personagem2
            hp_personagem1 = hp_personagem1 - dano_personagem2
            print('Resultado da rolagem de dano: ', dano_personagem2)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
            print('Total de pontos de vida restante do alvo: ', hp_personagem1)
            
            if(props_2 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))
              
                if(alternativa == 1):
                    dano_personagem2 = dado(8) + destreza_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-destreza_personagem2, '\nBonus de forca: ', destreza_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)
                else:
                    dano_personagem2 = dado(8) + forca_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)

        elif(damage_2 == 'd10'):
            dano_personagem2 = dado(10) + forca_personagem2
            hp_personagem1 = hp_personagem1 - dano_personagem2
            print('Resultado da rolagem de dano: ', dano_personagem2)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
            print('Total de pontos de vida restante do alvo: ', hp_personagem1)
            
            if(props_2 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))

                if(alternativa == 1):
                    dano_personagem2 = dado(10) + destreza_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-destreza_personagem2, '\nBonus de forca: ', destreza_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)

                else:
                    dano_personagem2 = dado(10) + forca_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)

        elif(damage_2 == 'd12'):
            dano_personagem2 = dado(12) + forca_personagem2
            hp_personagem1 = hp_personagem1 - dano_personagem2
            print('Resultado da rolagem de dano: ', dano_personagem2)
            print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                  dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
            print('Total de pontos de vida restante do alvo: ', hp_personagem1)
           
            if(props_2 == 'finesse'):
                alternativa = input(int(
                    'Como a arma do personagem possui a propriedade finesse, deseja utilizar o bonus de destreza ao inves do bonus de forca?\n1- Sim\n2-Nao'))
             
                if(alternativa == 1):
                    dano_personagem2 = dado(12) + destreza_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-destreza_personagem2, '\nBonus de forca: ', destreza_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)
                else:
                    dano_personagem2 = dado(12) + forca_personagem2
                    hp_personagem1 = hp_personagem1 - dano_personagem2
                    print('Resultado da rolagem de dano: ', dano_personagem2)
                    print('Detalhando bonus aplicados: \nRolagem de dados conforme arma: ',
                          dano_personagem2-forca_personagem2, '\nBonus de forca: ', forca_personagem2)
                    print('Total de pontos de vida restante do alvo: ',
                          hp_personagem1)

        else:
            print('Erro inesperado, reinicie o programa. ')
            return
    else:
        print('O ataque nao acertou')
    return hp_personagem1
# ----------------------------------------------------------------------------------------Fim /

# Função para o simulador do combate, que definirá o programa/// Inicio
def combate():
    print('\n\t\tSimulador de D&D: ')
    hp_personagem1 = personagem1["HP"]
    hp_personagem2 = personagem2["HP"]

    while(hp_personagem1 > 0 and hp_personagem2 > 0):
        if personagem1["dexterity"] > personagem2["dexterity"]:
            hp_personagem2 = ataque1vs2(hp_personagem2)
           
            if hp_personagem2 <= 0:
                break
            hp_personagem1 = ataque2vs1(hp_personagem1)

        elif personagem2["dexterity"] > personagem1["dexterity"]:
            hp_personagem1 = ataque2vs1(hp_personagem1)
            
            if hp_personagem1 <= 0:
                break
            hp_personagem2 = ataque1vs2(hp_personagem2)
        else:
            print('\nNão e possivel o combate entre personagens com a mesma destreza, reinicie o programa e tente novamente com outros personagens. ')
   
    if(hp_personagem1 > hp_personagem2):
        print('\n\tO combate se encerrou e o personagem : ',
              personagem2["name"], ' foi rendido! ')
        print('\n\tO personagem vencedor foi: ',
              personagem1["name"], 'com pontos de vidas restantes iguais a: ', hp_personagem1, '\n')

    elif(hp_personagem2 > hp_personagem1):
        print('\n\tO combate se encerrou e o personagem : ',
              personagem1["name"], ' foi rendido!')
        print('\n\tO personagem vencedor foi: ',
              personagem2["name"], 'com pontos de vidas restantes iguais a: ', hp_personagem2, '\n')

    else:
        print('\nEmpate!')
# ---------------------------------------------------------------------Fim da função /

# chamada da função de saída do simulador
combate()
# ---------------------------------------

