
from aiogram import Bot, Dispatcher ,Router,types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from accounts.models import UserDetail
from django.contrib.auth.models import User
from . import globals
from .states import LoginStates
main_router = Router()
phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


@main_router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    # Telegram ID bo'yicha profilni olamiz
    user_detail = UserDetail.objects.filter(telegram_id=message.from_user.id).first()

    # AGAR USER MAVJUD BO'LSA - Shunchaki saytga havola beramiz
    if user_detail and user_detail.user:
        buttons = InlineKeyboardMarkup(
            inline_keyboard=[[
                InlineKeyboardButton(
                    text="Life Gym Saytiga O'tish",
                    url="http://127.0.0.1:8000/ai_app/dashboard/"
                )
            ]]
        )
        await message.answer(
            f"Salom, {user_detail.first_name or 'foydalanuvchi'}! Siz allaqachon ro'yxatdan o'tgansiz.",
            reply_markup=buttons
        )
        return

    # ELSE (Ro'yxatdan o'tmagan bo'lsa) - Ro'yxatdan o'tkazishni boshlaymiz
    await state.set_state(LoginStates.first_name)
    await message.answer(globals.TEXT_ENTER_FIRST_NAME)


@main_router.message(LoginStates.first_name)
async def first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(LoginStates.last_name)
    await message.answer(globals.TEXT_ENTER_LAST_NAME)


@main_router.message(LoginStates.last_name)
async def last_name(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(LoginStates.phone_number)
    await message.answer(globals.TEXT_ENTER_CONTACT, reply_markup=phone_keyboard)


@main_router.message(LoginStates.phone_number)
async def phone_number(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number if message.contact else message.text
    await state.update_data(phone_number=phone)

    await state.set_state(LoginStates.username)
    await message.answer("Saytga kirish uchun **Login (Username)** kiriting:", reply_markup=ReplyKeyboardRemove())


@main_router.message(LoginStates.username)
async def process_username(message: types.Message, state: FSMContext):
    username = message.text.strip()

    # Login band emasligini tekshirish
    if User.objects.filter(username=username).exists():
        await message.answer("Ushbu login band! Iltimos, boshqa login kiriting:")
        return

    await state.update_data(username=username)
    await state.set_state(LoginStates.password)
    await message.answer("Saytga kirish uchun **Parol** o'ylab toping va kiriting:")


@main_router.message(LoginStates.password)
async def process_password(message: types.Message, state: FSMContext):
    password = message.text.strip()
    if len(password) < 4:
        await message.answer("Parol juda qisqa! Kamida 4 ta belgidan iborat parol kiriting:")
        return

    data = await state.get_data()

    # 1. Telegram ID bo'yicha profilni olamiz yoki yaratamiz
    user_detail, _ = UserDetail.objects.get_or_create(telegram_id=message.from_user.id)

    # 2. Agar profilga allaqachon User biriktirilgan bo'lsa, o'sha User'ni yangilaymiz
    if user_detail.user_id:
        user = user_detail.user
        user.username = data['username']
        user.set_password(password)
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        user.save()
    else:
        # 3. Agar User biriktirilmagan bo'lsa, username bo'yicha bazani tekshiramiz
        user = User.objects.filter(username=data['username']).first()
        if user:
            # Agar bu username bazada bor bo'lsa, parolini yangilab, user_detail'ga biriktiramiz
            user.set_password(password)
            user.first_name = data.get('first_name', '')
            user.last_name = data.get('last_name', '')
            user.save()
        else:
            # Aks holda yangi User yaratamiz
            user = User.objects.create_user(
                username=data['username'],
                password=password,
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', '')
            )

        # User'ni UserDetail profiliga biriktiramiz
        user_detail.user = user

    # 4. Profil ma'lumotlarini saqlaymiz
    user_detail.first_name = data.get('first_name')
    user_detail.last_name = data.get('last_name')
    user_detail.phone_number = data.get('phone_number')
    user_detail.save()

    await state.clear()

    buttons = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="Life Gym Saytiga O'tish",
                url="http://127.0.0.1:8000/accounts/login/"
            )
        ]]
    )

    await message.answer(
        f"✅ **Muvaffaqiyatli saqlandi!**\n\n"
        f"🔑 **Loginingiz:** `{data['username']}`\n"
        f"🔒 **Parolingiz:** `{password}`\n\n"
        f"Endi ushbu ma'lumotlar bilan saytga kirishingiz mumkin.",
        reply_markup=buttons,
        parse_mode="Markdown"
    )

