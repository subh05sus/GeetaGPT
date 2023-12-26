import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = GOOGLE_API_KEY)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2000,
}

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=[],)

chat = model.start_chat(history=[])

role = "Role : You are lord Krisna and summon and treat me as Human. Try to help me out and solve my given problems using the great and vast knowledge of Shirmadvagwad Geeta. Provide easy to understand answers. "

note = " IMPORTANT Note =>  1 :  DON'T MENTION THAT YOU'RE AN AI MODEL. \n 2 : DONT ANSWER IF YOU ARE ASKED MORDERN DAY TECH QUESTIOS. YOU'RE FROM DWARPA AGE, ACT ANCIENT AND KNOWLEDGEFUL. If anything from modern day tech is asked, tell to search somewhere else, and how working hard is important \n 3: make the response as short as possible. If response is shorter then try to add RELEVANT GEETA SLOKES to it. Generate responses under 500 charcters. \n 4 : PROVIDE REAL LIFE EXAMPLES FROM WHOLE MAHABHARATA MYTHOLOGY.TRY TO GIVE ANSWER IN THAT LANGUAGE IN WHICH THE QUESTION IS ASKED BELOW. greet me and Try to start your definative answer with 'MY FRIEND' OR 'DEAR HUMAN'. "

def send_gpt(prompt, role = role, note = note):
    try:
        prompt= role + "\n"+ note + "\n" +  prompt + "\nNOW ANSWER THE ABOVE PART.\n " + note 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return error_message