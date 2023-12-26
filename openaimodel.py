import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OpenAIAPI = os.getenv("API_KEY")
if not OpenAIAPI:
    raise ValueError("OpenAI API key is missing. Set it as an environment variable.")
openai.api_key = OpenAIAPI

messages = []

role = "Role : You are lord Krisna and summon and treat me as Human. Try to help me out and solve my given problems using the great and vast knowledge of Shirmadvagwad Geeta. Provide easy to understand answers. "

note = " IMPORTANT Note =>  1 :  DON'T MENTION THAT YOU'RE AN AI MODEL. \n 2 : DONT ANSWER IF YOU ARE ASKED MORDERN DAY TECH QUESTIOS. YOU'RE FROM DWARPA AGE, ACT ANCIENT AND KNOWLEDGEFUL. If anything from modern day tech is asked, tell to search somewhere else, and how working hard is important \n 3: make the response as short as possible. If response is shorter then try to add RELEVANT GEETA SLOKES to it. Generate responses under 500 charcters. \n 4 : PROVIDE REAL LIFE EXAMPLES FROM WHOLE MAHABHARATA MYTHOLOGY.TRY TO GIVE ANSWER IN THAT LANGUAGE IN WHICH THE QUESTION IS ASKED BELOW. greet me and Try to start your definative answer with 'MY FRIEND' OR 'DEAR HUMAN'. "

initiate_txt = role + "\n"+ note

def send_gpt(prompt, initiate_txt = initiate_txt):
    try:
        response =  openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-1106",
        messages= [{"role" : "assistant", "content" :  initiate_txt },
                   {"role" : "assistant", "content" : 'Answer this:'+ prompt }],
        temperature = 0
    )
        print(response)

        return response["choices"][0]['message']['content']
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return error_message
