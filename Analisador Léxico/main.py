# tk.tokeniza(), 
import esqueleto_tokeniza as tk

# categorias e dicionario "categoria: decrição" 
import operadores as op


def primeiroTwitch():
      text = "Eu reclamo de ser adulto, mas o problema mesmo é ser pobre. Ser adulto com dinheiro deve ser muito bom."
      tk.tokeniza(text)

      for token, categoria in tk.analysis:
            print(f"Token: {token} | Categoria: {categoria}")

primeiroTwitch()

#def segundoTwitch():
 #     text = """
  #      Examinando o paciente com o oxímetro:
   #         - 66? Meu oxigênio tá 66? Isso tá muito baixo, não tá não?
    #        - Não sr, tá 99%, é que você tá vendo de cabeça pra baixo..
     #   Não julgo pois sou ansioso igual
      #"""
      #tk.tokeniza(text)

      #for token, categoria in tk.analysis:
       #     print(f"Token: {token} | Categoria: {categoria}")


print('=================================================')
print('=                                               =')
print('=================== SEPARANDO ===================')
print('=                                               =')
print('=================================================')
#segundoTwitch()

