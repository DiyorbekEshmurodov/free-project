from django.apps import AppConfig
import threading
import os


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Server qayta yuklanganda bot 2 marta ishga tushmasligi uchun tekshiruv
        if os.environ.get('RUN_MAIN') == 'true':
            from run_bot import main
            import asyncio

            def start_bot():
                asyncio.run(main())

            threading.Thread(target=start_bot, daemon=True).start()