import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key :
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"
role = "user"

prompt = " suggest a name for printing kiosk startup which will not create problem in trademark , and also suggest domain name for the same startup."

message_system = {
    "role" :"system",
    "content" : "You are my brand manager , help me to suggest name for my startup , which will not create problem in trademark ."
}


message ={
    "role":role,
    "content":prompt
}

message = [message_system , message]

#temprature is a parameter that controls the randomness of the model's output. A higher temperature (e.g., 1.0) will make the output more random, while a lower temperature (e.g., 0.2) will make it more focused and deterministic.    
response = client.chat.completions.create(model=model, messages=message, temperature=1)
# print(response)
print(response.choices[0].message.content)