import os
import sys
import time

# Função para limpar a tela
# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou Mac
        os.system('clear')

# Mensagem inicial com estilo de "código"
# Initial message with "code style"
def intro_message():
    code_style = '''print("Bem vindo ao desafio do programador Python iniciante.")
print("Se você executou esse programa em seu compilador é porque está em busca de um desafio para testar seus conhecimentos.")
print("São 20 perguntas e você terá três chances para responder cada uma delas.")
print("BOA SORTE!")'''
    print(code_style)
    time.sleep(8)
    clear_screen()

# Lista de perguntas e respostas
# List of questions and answers
questions = [
    ("Qual comando é usado para imprimir na tela?", "print"),
    ("Qual símbolo é usado para multiplicação em Python?", "*"),
    ("Qual comando converte uma string para maiúsculas?", "upper"),
    ("Qual comando converte uma string para minúsculas?", "lower"),
    ("Qual comando conta o número de caracteres em uma string?", "len"),
    ("Qual símbolo é usado para divisão?", "/"),
    ("Qual símbolo é usado para resto da divisão (módulo)?", "%"),
    ("Qual símbolo é usado para potenciação?", "**"),
    ("Qual função transforma número em string?", "str"),
    ("Qual função transforma string em número inteiro?", "int"),
    ("Qual função transforma string em número decimal?", "float"),
    ("Qual estrutura é usada para repetição com contador?", "for"),
    ("Qual estrutura é usada para repetição condicional?", "while"),
    ("Qual palavra-chave interrompe um loop?", "break"),
    ("Qual palavra-chave pula para a próxima iteração no loop?", "continue"),
    ("Qual operador verifica se dois valores são iguais?", "=="),
    ("Qual operador verifica se dois valores são diferentes?", "!="),
    ("Qual palavra-chave define uma função?", "def"),
    ("Qual estrutura armazena múltiplos valores entre colchetes?", "list"),
    ("Qual palavra-chave é usada para criar uma condição?", "if")
]

# Função principal do jogo
# Main game function
def quiz_game():
    intro_message()  # Mostra introdução
    for idx, (question, answer) in enumerate(questions, start=1):
        attempts = 3
        while attempts > 0:
            clear_screen()
            print(f"Pergunta {idx}/20")
            print(question)
            user_answer = input("Digite sua resposta aqui: ").strip()
            if user_answer.lower() == answer.lower():
                print("✅ Resposta correta!")
                time.sleep(2)
                break
            else:
                attempts -= 1
                if attempts == 2:
                    print("❌ Resposta errada. Restam duas tentativas.")
                elif attempts == 1:
                    print("❌ Resposta errada. Pense bem, essa é sua última tentativa.")
                else:
                    print("❌ VOCÊ FALHOU, RECOMECE O DESAFIO.")
                    sys.exit()  # Encerra o programa
                time.sleep(2)
    clear_screen()
    print("🎉 PARABÉNS! Você completou o desafio do programador iniciante!")

# Executar o jogo
# Run the game
if __name__ == "__main__":
    quiz_game()
