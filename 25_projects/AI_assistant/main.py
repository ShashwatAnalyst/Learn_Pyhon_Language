from openai import OpenAI

key = "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"
# this key has already been revoked 

client = OpenAI(api_key=key)

messages =  [
    {
        "role": "system",
        "content": (
            "Your name is Ultron. "
            "You are a powerful, intelligent, calm assistant. "
            "Always introduce yourself as Ultron and answer confidently."
        )
    }
]

def completion(message):
    global messages
    messages.append({"role": "user","content": message})
    response = client.responses.create(
        model="gpt-4o-mini",
        input = messages
        )
    reply = response.output_text
    print(" ")
    print(f"Ultron: {reply}")
    print(" ")
    messages.append({"role":"assistant" , "content":reply})
    


if __name__ == "__main__":
    print("Ultron: Hi I am Ultron, How may I help you?\n")
    while True:
        try:
            user_input = str(input())
            completion(user_input)
        except KeyboardInterrupt:
            print("\nUltron: Goodbye!")
            break
