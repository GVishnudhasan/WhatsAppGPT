from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")


def ai_response(input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input,
        temperature=0.75,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    print(response.choices[0].text)
    return response.choices[0].text
