from dotenv import load_dotenv
import os
from groq import Groq
import json
load_dotenv()

def generate_user_advice(self,profile,card_id,period,user_plans):
    buyi = getattr(profile,'buyi','Nomalum')
    vazni = getattr(profile,'vazni','Nomalum')
    maqsadi = getattr(profile,'maqsadi','Nomalum')

    client = Groq(api_key=os.getenv("API_KEY"))

    prompt = f"""
        Siz professional fitness va ovqatlanish bo'yicha sun'iy intellekt murabbiyisiz.
        Foydalanuvchi ma'lumotlari:
        - Bo'yi: {buyi} cm
        - Vazni: {vazni} kg
        - Maqsadi: {maqsadi}
        - Tanlangan yo'nalish (karta): {card_id}
        - Davriylik: {period}

        Quyidagi JSON formatida FAQAT va FAQAT toza JSON javob qaytaring (hech qanday ortiqcha matnsiz):
        {{
            "nutrition": "Foydalanuvchining bo'yi, vazni va maqsadi uchun aniq kaloriya, oqsil hamda suv miqdori bo'yicha tavsiya",
            "workout": "Ushbu maqsad va davr uchun mos keladigan aniq mashqlar va ularning takrorlanishlar soni",
            "ai_recommendation": "Tiklanish, uyqu va natijaga erishish bo'yicha muhim maslahat"
        }}
        """
    try :
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Groq'ning eng kuchli modeli
            messages=[
                {"role": "system", "content": "Siz faqat valid JSON formatida javob beradigan AI assistentisiz."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            response_format={"type": "json_object"}
        )
        advice_json = json.loads(completion.choise[0].message.content)
        return advice_json
    except Exception as e:
        print("Groq API Xatolik: ",e)

        return {
            "nutrition": f"Ratsioningizda oqsilni oshiring va kamida {float(vazni) * 35 / 1000 if str(vazni).replace('.', '', 1).isdigit() else 2}L suv iching.",
            "workout": "Haftasiga 3 marta mashg'ulot bajaring.",
            "ai_recommendation": "Kunlik uyqu va ovqatlanish rejimiga amal qiling."
        }