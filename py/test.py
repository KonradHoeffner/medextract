import requests
import os

ENDPOINT = "https://api.helmholtz-blablador.fz-juelich.de/v1/completions"
PAT = os.getenv("HELMHOLTZ_PAT")
if not PAT:
    raise ValueError("HELMHOLTZ_PAT environment variable not set.")


def completion(s):
    headers = {"Authorization": f"Bearer {PAT}"}
    data = {
        # "model": "alias-large", # for production
        "model": "alias-fast",  # for testing
        "prompt": s,
        "suffix": "string",
        "temperature": 0.7,
        "n": 1,
        "max_tokens": 160,
        "stop": "string",
        "stream": False,
        "top_p": 1,
        "top_k": -1,
        "logprobs": 0,
        "echo": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "user": "string",
        "use_beam_search": False,
        "best_of": 0,
        "seed": 0,
    }
    response = requests.post(ENDPOINT, json=data, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")


completion("The best ice cream is:")
