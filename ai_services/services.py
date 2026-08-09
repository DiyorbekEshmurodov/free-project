import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import *
load_dotenv()
API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)
def ai_handler(buyi,vazni,goal):
    prompt_text =  get_fitness_prompt(vazni, buyi, goal)
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt_text)

        return response.text

    except Exception as e:
        print(f"AI bilan bog'lanishda xatolik: {e}")
        return None