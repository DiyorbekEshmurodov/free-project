def get_fitness_prompt(vazni, buyi, maqsadi):
    """
    Foydalanuvchi ma'lumotlarini olib, AI uchun aniq shablon va 
    JSON formatda javob berishini talab qiluvchi prompt qaytaradi.
    """
    prompt = f"""
    Siz professional fitness va diyetolog mutaxassisiz.
    Quyidagi ko'rsatkichlarga ega foydalanuvchi uchun tahlil tuzing:

    - Vazni: {vazni} kg
    - Bo'yi: {buyi} sm
    - Maqsadi: {maqsadi}

    1:
    {{
      "calories": "Tavsiya qilinadigan kunlik kaloriya miqdori",
      "dietolog": "Qisqacha taomnoma tavsiyasi",
      "workout": "Mashqlar rejasi tavsiyasi"
    }}
    """
    return prompt.strip()