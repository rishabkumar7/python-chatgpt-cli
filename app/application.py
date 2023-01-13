import os
import logging
import openai

if openai.api_key:
    logging.info(f"Proceeding since environment variable OPENAI_API_KEY exists {openai.api_key=}")
    pass
else:
    openai.api_key = input("Please input your OpenAI API key.")
    pass

openai.api_key = os.getenv("OPENAI_API_KEY")

def chatgpt():
    chatgpt_ques = input("Ask ChatGPT 🤖 \n")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatgpt_ques,
        max_tokens=3000,
        temperature=0.7
    )
    """Respond to question with ChatGPT's response."""
    print(response["choices"][0]["text"])

    return str(response)

chatgpt();