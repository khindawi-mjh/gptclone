import openai

openai.api_key = "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"
models = openai.Model.list()
print([model["id"] for model in models["data"]])