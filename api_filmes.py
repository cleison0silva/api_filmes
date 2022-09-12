import requests  #importando biblioteca de requisições
import json     #importando biblioteca jason

#função para fazer a requisão do título do filme

def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?apikey=3341638b&t=" + titulo + "&type=movie")
        info = json.loads(req.text)
        return info
    except:
        print("Erro na Conexão")
        return None

#função para imprimir os detalhes

def printar_detalhes(filme):
    print("Título: ", filme["Title"])
    print("Ano: ", filme["Year"])
    print("Diretor: ", filme["Director"])
    print("Atores: ", filme["Actors"])
    print("Nota: ", filme["imdbRating"])
    print("Prêmio", filme["Awards"])
    print("Foto: ", filme["Poster"])
    print(" ")

#programa com laço de repetição

sair = False
while not sair:
    op = input("Escreva o nome de um filme ou SAIR para fechar: ")

    if op == "SAIR":
        print("Saindo...")
        sair = True
    else:
        filme = requisicao(op)
        if filme["Response"] == "False":
            print("Filme não econtrado")
        else:
            printar_detalhes(filme)

