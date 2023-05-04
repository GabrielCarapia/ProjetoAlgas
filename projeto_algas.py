import time 
from sys import getsizeof
import random
from conexao import criar_conexao, fechar_conexao



def insere_dado(con, nameUsuario, perc_oxygen):
    cursor = con.cursor()
    sql = "INSERT INTO percOfoxygen (nameUsuario, perc_oxygen) VALUES (%s, %s)"
    valores = (nameUsuario, perc_oxygen)
    cursor.execute(sql, valores)
    cursor.close()
    con.comit()


def insere_dado_dois(con, tempo_exec, max_mem, min_mem):
    cursor = con.cursor()
    sql = "INSERT INTO machine_info (tempo_exec, max_mem, min_mem) VALUES (%s, %s, %s)"
    valores = (tempo_exec, max_mem, min_mem)
    cursor.execute(sql, valores)
    cursor.close()
    con.comit()


l1 = []


def calcula_porc_o2(n, v):
    con = criar_conexao("localhost", "root", "urubu100", "oximetro")
    for i in range(n, v, n):
        data = 'x' * i
        b = data
        #for j in i:
        #   print(j)
        a = random.randint(80, 100)
        if a >= 96:
            print(f'Sinal Verde: {a}')
        elif a > 90 & a < 96:
            print(f'Sinal Amarelo: {a}')
        else:
            print(f'Sinal Vermelho: {a}')
        #print(a)
        start = time.time()
        mex_mem = 0
        min_mem = 0
        while b:
            if i == len(b):
                max_mem = getsizeof(b) - getsizeof('')
            elif len(b) == 1:
                min_mem = getsizeof(b) - getsizeof('')
            b = b[1:] 
        stop = time.time()
        #print('Valor {n} {stop-start} - Max mem {max_mem/10**3} Kb - Min mem {min_mem} B')
        l1.append(stop-start)
        insere_dado_dois(con, stop-start, (max_mem/10**3), min_mem)
        insere_dado(con, "carapia02211018", a)
    fechar_conexao(con)



calcula_porc_o2(1, 1441)
#calcula_porc_o2(3, 4321)
#calcula_porc_o2(5, 7201)
#calcula_porc_o2(10, 14401)
#calcula_porc_o2(50, 72001)