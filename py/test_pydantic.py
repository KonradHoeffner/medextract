import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

ENDPOINT = "https://api.helmholtz-blablador.fz-juelich.de/v1/completions/"
PAT = os.getenv("HELMHOLTZ_PAT")
if not PAT:
    raise ValueError("HELMHOLTZ_PAT environment variable not set.")

model = OpenAIChatModel(
    "alias-fast",
    provider=OpenAIProvider(base_url=ENDPOINT, api_key=PAT),
)

agent = Agent(model)

result = agent.run_sync('Where does "hello world" come from?')


print(result.output)
"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""
