from groq import Groq
from django.conf import settings


def ai_handler(prompt_text):
    # settings.py orqali .env faylingizdagi GROQ_API_KEY olinadi
    api_key = settings.GROQ_API_KEY

    if not api_key:
        return "Xatolik: GROQ_API_KEY topilmadi. .env faylingizni tekshiring."

    try:
        client = Groq(api_key=api_key)

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Siz professional diyetolog va shaxsiy fitnes trenergiz. Javoblaringizni o'zbek tilida, tushunarli va chiroyli formatda bering."
                },
                {
                    "role": "user",
                    "content": prompt_text,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Groq AI bilan bog'lanishda xatolik yuz berdi: {str(e)}"