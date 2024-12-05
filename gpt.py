import openai

openai.api_key = ""
models = openai.Model.list()
print([model["id"] for model in models["data"]])