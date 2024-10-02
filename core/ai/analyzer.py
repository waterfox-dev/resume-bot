import openai
from core.struct.message_pool import MessagePool

class Analyzer:

    def __init__(self, message_pool: MessagePool, api_key: str):
        self.message_pool = message_pool
        openai.api_key = api_key

    def analyze(self):
        prompt = (
            f"Résumez les messages suivants. Veuillez faire attention à qui parle. Résumez le point de vue de chaque personne :\n\n"
            + "\n\n".join(
            [
                f"{message.author} - {message.content}"
                for message in self.message_pool
            ]
            ) + "\n\n Vous pouvez utiliser le markdown pour formater le texte."
        )
        
        response = openai.chat.completions.create(
            model="gpt-4o",
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
