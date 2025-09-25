from blablador import Models, Completions, ChatCompletions, TokenCount
import ast
import glob

corpus = glob.glob("grassco/*.txt")

import os

API_KEY = os.getenv("HELMHOLTZ_PAT")
if not API_KEY:
    raise ValueError("HELMHOLTZ_PAT environment variable not set.")
MODEL = "alias-fast"


with open(corpus[0], "r") as file:
    doc = file.read()

print("generating ontology for:\n" + doc)

# Retrieve available models
# models = Models(api_key=API_KEY).get_model_ids()
# returns: ['Marcoroni-70B', 'Mistral-7B-Instruct-v0.1', 'openchat_3.5', 'zephyr-7b-beta']

# Generate chat completions
# completion = ChatCompletions(api_key=API_KEY, model=models[3])
print("*********************")
completion = ChatCompletions(api_key=API_KEY, model=MODEL)
response = completion.get_completion(
    [
        {"role": "user", "content": doc},
        {
            "role": "system",
            "content": "You are an expert ontology designer and return only an OWL ontology in Turtle serialization for the given input, do not return any message.",
        },
    ]
)
# Returns a JSON string

print(ast.literal_eval(response)["choices"][0]["message"]["content"])
# {'role': 'assistant', 'content': "I'm not capable of experiencing emotions or having a physical body, but...
