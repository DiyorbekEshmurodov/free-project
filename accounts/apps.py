import os
import threading
import asyncio
import subprocess
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Server qayta yuklanganda bot va ngrok 2 marta ishga tushmasligi uchun tekshiruv
        if os.environ.get('RUN_MAIN') == 'true':
            from run_bot import main

            # 1. Ngrok-ni fonda ishga tushirish
            def start_ngrok():
                subprocess.Popen(["ngrok", "http", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # 2. Botni ishga tushirish
            def start_bot():
                asyncio.run(main())

            # Ikkala jarayonni ham alohida thread'larda yuritish
            threading.Thread(target=start_ngrok, daemon=True).start()
            threading.Thread(target=start_bot, daemon=True).start()