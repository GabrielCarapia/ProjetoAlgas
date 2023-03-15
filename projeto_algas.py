import time 
from sys import getsizeof
import random
from conexao import criar_conexao, fechar_conexao


def insere_dado(con, id, porc_o2):
    cursor = con.cursor()
    sql = "INSERT INTO porc_o2_sangue (id, porc_o2) values (%d, %d)"
    valores = (id, porc_o2)
    cursor.execute(sql, valores)
    cursor.close()
    con.comit()

l1 = []
l2 = []
countVerde = 0
countAmarelo = 0
countVermelho = 0

def main():
    con = criar_conexao("localhost", "root", "Gcc#77801", "oximetro")
    for n in range(1, 10, 1):
        data = 'x' * n 
        b = data
        #print(b)
        start = time.time()
        max_mem= 0
        min_mem = 0
        while b:
            if n == len(b):
                max_mem = getsizeof(b) - getsizeof('') 
            elif len(b) == 1:
                min_mem = getsizeof(b) - getsizeof('')
            b = b[1:]
        stop = time.time()
        a = random.randint(80, 100)
        if a >= 96:
            print(f'Sinal Verde: {a}')
            countVerde = countVerde + 1
        elif a > 90 & a < 96:
            print(f'Sinal Amarelo: {a}')
            countAmarelo = countAmarelo + 1
        else:
            print(f'Sinal Vermelho: {a}')
            countVermelho = countVermelho + 1
        #print(f'O2 Verde: {countVerde}')
        #print(f'O2 Amarelo: {countAmarelo}')
        #print(f'O2 Vermelho: {countVermelho}')
        l1.append(stop-start)
        insere_dado(con, n, a)
    #print(f'Valor {n} {stop-start} - Max mem {max_mem/10**3} Kb - Min mem {min_mem} B')
    fechar_conexao(con)


#range(1, 1441) -- 1 usuário
#range(1, 4321) -- 3 usuários
#range(1, 7201) -- 5 usuários
#range(1, 14401) -- 10 usuários
#range(1, 72001) -- 50 usuários







