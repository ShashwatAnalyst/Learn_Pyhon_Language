from openai import OpenAI

key = "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"
# this key has already been revoked 

client = OpenAI(api_key=key)

response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me a cat joke"
)

# Correct way to print the actual text
print(response.output[0].content[0].text)
