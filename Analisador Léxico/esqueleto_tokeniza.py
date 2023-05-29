import operadores
import re
# Constantes
TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r', '@']

# caractere que indica comentário
COMENTARIO = "#"
analysis = []

#------------------------------------------------------------
def tokeniza(text):
    tokens = re.findall(r'\b\w+\b', text, re.IGNORECASE)
    

    for token in tokens:
        for palavra, categoria in operadores.LEXICON.items():
            if re.match(palavra, token, re.IGNORECASE):
                analysis.append((token, categoria))
                break
        else:
            analysis.append((token, 'DESCONHECIDO'))

    return analysis
    # escreva o seu código abaixo
    
    
