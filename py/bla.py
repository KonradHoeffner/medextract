from blablador import Models, Completions, ChatCompletions, TokenCount
import ast

import os

API_KEY = os.getenv("HELMHOLTZ_PAT")
if not API_KEY:
    raise ValueError("HELMHOLTZ_PAT environment variable not set.")

# Retrieve available models
models = Models(api_key=API_KEY).get_model_ids()
# returns: ['Marcoroni-70B', 'Mistral-7B-Instruct-v0.1', 'openchat_3.5', 'zephyr-7b-beta']

# Generate completions
completion = Completions(api_key=API_KEY, model=models[3])
response = completion.get_completion("The best cuisine in the world is")
# Returns a JSON string


# Generate chat completions
completion = ChatCompletions(api_key=API_KEY, model=models[3])
response = completion.get_completion(
    [{"role": "user", "content": "Hello, how are you?"}]
)
# Returns a JSON string

print(ast.literal_eval(response)["choices"][0]["message"])
# {'role': 'assistant', 'content': "I'm not capable of experiencing emotions or having a physical body, but...

# Count tokens in a text
token_count = TokenCount(model=models[3]).count("Count this yo!")
# Returns the number of tokens in a JSON string
