import openai
from core.struct.message_pool import MessagePool

class Analyzer:

    def __init__(self, message_pool: MessagePool, api_key: str):
        self.message_pool = message_pool
        openai.api_key = api_key

    def analyze(self) -> str:
        prompt = (
            f"""Résumé des messages suivants. Identifiez qui parle et ne gardez que les points de vue pertinents :\n\n"""
            + "\n\n".join(
            [f"{message.author}: {message.content}" for message in self.message_pool]
            ) + """\n\nUtilisez markdown. Soyez direct et concis, sans détails superflus ni espaces inutiles. 
            Allez à l'essentiel uniquement. 
            La structure de ton document est 'point de vue {{user 1}}\n point de vue de {{user2}}\n...\n point de vue de {{userN}}' \n Résumé:"""
        )
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt}
            ],
            max_tokens=256,
            n=1,
            stop=None,
            temperature=0.7
        )
        
        summary = response.choices[0].message.content
        return summary
