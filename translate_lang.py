import openai
from decouple import config

openai.api_key = config('OPENAI_API_KEY')

def get_translation(text, lang):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt= f"Translate this into {lang}\n\n{text}",
        temperature=0.3,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        return response.choices[0].text
    except:
        return "Houston, we have a problem"