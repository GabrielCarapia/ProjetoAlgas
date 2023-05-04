import time 
from sys import getsizeof
import random
from conexao import criar_conexao, fechar_conexao
import dis
import timeit


def insere_dado(con, nameUsuario, id, porc_o2):
    cursor = con.cursor()
    sql = "INSERT INTO porc_o2_sangue (id, nameUsuario, perc_oxygen) VALUES (%d, %d, %d)"
    valores = (id, nameUsuario, porc_o2)
    cursor.execute(sql, valores)
    cursor.close()
    con.comit()


l1 = []


def calcula_porc_o2(n, v):
    con = criar_conexao("python-mysql", "root", "urubu100", "oximetro")
    for i in range(n, v, n):
        data = 'x' * i
        b = data
        for j in i:
            print(j)
            a = random.radint(80, 100)
            if a >= 96:
                #print(f'Sinal Verde: {a}')
                countVerde = countVerde + 1
            elif a > 90 & a < 96:
                #print(f'Sinal Amarelo: {a}')
                countAmarelo = countAmarelo + 1
            else:
                #print(f'Sinal Vermelho: {a}')
                countVermelho = countVermelho + 1
            print(a)
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

        print('Valor {n} {stop-start} - Max mem {max_mem/10**3} Kb - Min mem {min_mem} B')
        l1.append(stop-start)
        insere_dado(con, "carapia02211018", i, a)
    fechar_conexao(con)



calcula_porc_o2(1, 1441)
calcula_porc_o2(3, 4321)
calcula_porc_o2(5, 7201)
calcula_porc_o2(10, 14401)
calcula_porc_o2(50, 72001)