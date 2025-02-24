import os
from dotenv import main
from mistralai import Mistral

main.load_dotenv()
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")
api_key = os.environ["MISTRAL_API_KEY"]
model = "open-mistral-7b"
client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "你會說中文嗎？",
        },
    ],
)
print(chat_response.choices[0].message.content)
