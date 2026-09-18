import os
from dotenv import load_dotenv
import time
from openai import OpenAI

client = OpenAI(api_key=os.getenv("CLIENT_KEY"))

while True:
    question = input("\nYour question: ")

    if question.lower() == "exit":
        break

    response = client.responses.create(
        model="gpt-5-mini",
        input=question,
    )

    print("AI:",response.output_text)
    time.sleep(2)