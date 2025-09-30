"""
Jogo de Adivinhação em Python

Um jogo interativo onde o jogador tenta adivinhar um número secreto
com diferentes níveis de dificuldade e sistema de pontuação.

Autor: Ariel de Freitas Silva
Data: 30/09/2025
Versão: 1.0
"""

import random
import os   

print("\nOlá! Para começarmos, digite o seu nome. ")
nome = input("Seu nome: ")

print(f"\nOlá {nome}! Vamos jogar!")

def menu_principal():
    historico_de_partidas = []

    while True:
        
        print("\n" + "="*31)
        print("===== JOGO DE ADIVINHAÇÃO =====")
        print("="*31)
        print("1. Jogar")
        print("2. Ver histórico de partidas")
        print("3. Instruções")
        print("4. Sair")

        escolha = input("\nO que deseja fazer ?")

        if escolha == '1':
            resultado = dificuldade()
            if resultado:
                historico_de_partidas.append(resultado)
        elif escolha == '2':
            mostrar_historico(historico_de_partidas)
        elif escolha == '3':
            instrucoes()
        elif escolha == '4':
            print(f"\nObrigado por jogar, {nome}! Até logo! 👋")      
            break
        else:
            print("❌ Opção inválida! Escolha entre 1 e 4.")
        
def mostrar_historico(historico):
    if not historico:
        print("\n📊 Nenhuma partida foi jogada ainda.")
        return

    print("\n" + "="*33)
    print("===== HISTÓRICO DE PARTIDAS =====")
    print("="*33)

    for i, partida in enumerate (historico,1):
        resultado = "✅ VITÓRIA" if partida["venceu"] else "❌ DERROTA"
        print(f"\nPartida {i}:")
        print(f"  Dificuldade: {partida['dificuldade']}")
        print(f"  Número secreto: {partida['numero_secreto']}")
        print(f"  Tentativas usadas: {partida['tentativas']}/{partida['max_tentativas']}")
        print(f"  Resultado: {resultado}")
        print(f"  Pontuação: {partida['pontuacao']} pontos")
    
    input("\nPressione Enter para voltar...")


def instrucoes():
    while True:
        print("\n" + "="*28)
        print("====INSTRUÇÕES DE JOGO====")
        print("="*28)
        print("\n1. O computador gera um número secreto")
        print("2. Você deve adivinhar qual é o número")
        print("3. A cada palpite, você recebe dicas:")
        print("   - 'MAIOR!': seu número é menor que o secreto")
        print("   - 'MENOR!': seu número é maior que o secreto")
        print("4. Quanto menos tentativas, mais pontos!")

        voltar = input("\nPressione ENTER para voltar...")
        break

def dificuldade():
    print("\n" + "="*31)
    print("====SELECIONE A DIFICULDADE====")
    print("="*31)
    print("1. Fácil (10 tentativas) - Números: 1-50")
    print("2. Médio (7 tentativas) - Números: 1-100")
    print("3. Difícil (5 tentativas) - Números: 1-200")


    while True:
        dificuldade = input("Escolha a dificuldade: ")

        if dificuldade == '1':
            return jogo_advinhacao(10,50,"Fácil")
        elif dificuldade =='2':
            return jogo_advinhacao(7,100,"Médio")
        elif dificuldade == '3':
            return jogo_advinhacao(5,200,"Difícil")
        else:   
            print("❌ Opção inválida! Escolha entre 1 e 3.")

def jogo_advinhacao(max_tentativas, limite, dificuldade_nome):
    
        numero_secreto = random.randint(1,limite)
        tentativas = 0
        venceu = False
        pontuacao = 0

        print(f"\n🎯 Dica: É um número entre 1 e {limite} .")
        print(f"💡 Você tem {max_tentativas} tentativas")
        print(f"📊 Dificuldade: {dificuldade_nome}")

        while tentativas < max_tentativas: 
                try:  
                    palpite = int(input("\nSeu Palpite:"))
                    tentativas += 1

                    if palpite < 1 or palpite > limite:
                        print(f"❌ Digite um número entre 1 a {limite}!")
                        continue

                    if palpite < numero_secreto:
                        print(f"📈 MAIOR! Tente um número maior. Tentativas restantes {max_tentativas - tentativas} ")
                    elif palpite > numero_secreto:
                        print(f"📉 MENOR! Tente um número menor. Tentativas restantes {max_tentativas - tentativas} ")
                    else: 
                        print(f"\n🎉 PARABÉNS {nome} !!! Você acertou o número em {tentativas} tentativas!!!")

                        venceu = True

                        if dificuldade_nome == "Fácil":
                            pontuacao = max(100 - tentativas * 5, 10)
                        elif dificuldade_nome == "Médio":
                            pontuacao = max(150 - tentativas * 10, 20)
                        else:  # Difícil
                            pontuacao = max(200 - tentativas * 15, 30)
                    
                        print(f"🏆 Sua pontuação: {pontuacao} pontos!")
                        break
                        

                except ValueError:
                    print("Número Inválido!")

        if not venceu:
            print(f"\n💔 Fim de jogo! O número era {numero_secreto}")
            pontuacao = 0

        return{
            "dificuldade": dificuldade_nome,
            "numero_secreto": numero_secreto,
            "tentativas": tentativas,
            "max_tentativas": max_tentativas,
            "venceu": venceu,
            "pontuacao": pontuacao
        }


if __name__ == "__main__":
    menu_principal()