
from json import JSONEncoder
import openai
from pywebio import start_server
from pywebio.output import put_table, put_code
from pywebio.input import input
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def openai_response(question):

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=question,
        temperature=0.8,
        max_tokens=1000,
    )
    print(response.choices)
    print(response, '{}'.format(response.choices[0].text[6:]))
    # return '{}'.format(response.choices[0].text[6:])
    return response.choices[0].text
def index():
    while True:
        question = input('Describe your desired code')
        put_table([
            ['Description:', question],
            ['Code:', put_code(openai_response(question), language="typescript")]
        ])
def applyToQuote():
    print('endpoint hit')
    return openai_response('What is five plus 7? ')


if __name__ == '__main__':
    port = os.environ.get("PORT", 8080)
    start_server([index, applyToQuote], port=port, debug=True)