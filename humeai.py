import asyncio
from hume import HumeStreamClient
from hume.models.config import LanguageConfig
from config import API_KEY

samples = [
    "Je suis content de pouvoir naviguer facilement sur ce site web, mais j'aimerais avoir un peu plus d'options de personnalisation.",
    "Cette application me semble très facile à utiliser, mais je pense que certains éléments pourraient être améliorés.",
    "Bien que j'apprécie la rapidité de chargement du site, je trouve que le contenu manque un peu de pertinence.",
    "Les fonctionnalités de cette plateforme sont impressionnantes, mais j'ai rencontré quelques difficultés techniques en les utilisant.",
    "Je suis très satisfait des services proposés par cette entreprise, mais j'aimerais avoir une meilleure communication avec le support client.",
    "Je suis un peu inquiet à propos de la sécurité de mes données, mais je suis content de voir que le site utilise le protocole HTTPS.",
    "J'ai trouvé les instructions pour créer un compte un peu confus, mais après avoir cherché un peu j'ai fini par comprendre.",
    "J'ai eu du mal à trouver l'option que je cherchais, mais une fois que je l'ai trouvée, c'était facile à utiliser",
    "Je suis un peu déçu de voir que certaines fonctionnalités que j'attendais ne sont pas disponibles sur ce site, mais je comprends que cela puisse être dû à des contraintes techniques."
]


async def main():
    client = HumeStreamClient(API_KEY)
    config = LanguageConfig()

    async with client.connect([config]) as socket:
        for i in range(len(samples)):
            phrase = samples[i].strip()

            result = await socket.send_text(phrase)
            emotions = result["language"]["predictions"][0]["emotions"]

            top_emotions = sorted(
                emotions, key=lambda x: x["score"], reverse=True)[:3]
            top_emotion_names = [emotion["name"] for emotion in top_emotions]
            print(f"Phrase: {phrase}")
            print("Top Emotions:", top_emotion_names)
            print("-------------------------")

asyncio.run(main())
