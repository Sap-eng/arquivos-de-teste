import requests

def buscar_filmes():
    url = "https://ghibliapi.vercel.app/films"

    resposta = requests.get(url)
    filmes = resposta.json()

    print("\n🎬 Filmes disponíveis:\n")

    for filme in filmes:
        print(f"- {filme['title']}")

buscar_filmes()