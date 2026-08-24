
from aiogram import Bot, Dispatcher ,Router,types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from accounts.models import UserDetail
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
async def start(message: types.Message,state: FSMContext):
    user= UserDetail.objects.filter(telegram_id=message.from_user.id).first()
    if not user or not user.first_name :
        await state.set_state(LoginStates.first_name)
        await message.answer(globals.TEXT_ENTER_FIRST_NAME)
    elif not user.last_name :
        await state.set_state(LoginStates.last_name)
        await message.answer(globals.TEXT_ENTER_LAST_NAME)
    elif not user.phone_number :
        await state.set_state(LoginStates.phone_number)
        await message.answer(globals.TEXT_ENTER_CONTACT)
    else:
        buttons = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Xush kelibsiz! Saytga o'tish",
                        url="http://127.0.0.1:8000/ai_app/dashboard/"
                    )
                ]
            ]
        )
        await message.answer(text=globals.WELCOME_TEXT, reply_markup=buttons)


@main_router.message(LoginStates.first_name)
async def first_name(message: types.Message,state: FSMContext):
    user,created = UserDetail.objects.get_or_create(telegram_id=message.from_user.id)
    user.first_name = message.text
    user.save()
    await state.set_state(LoginStates.last_name)
    await message.answer(globals.TEXT_ENTER_LAST_NAME)

@main_router.message(LoginStates.last_name)
async def last_name(message: types.Message,state: FSMContext):
    user = UserDetail.objects.filter(telegram_id=message.from_user.id).first()
    if user:
        user.last_name = message.text
        user.save()
    await state.set_state(LoginStates.phone_number)
    await message.answer(
        globals.TEXT_ENTER_CONTACT,
        reply_markup=phone_keyboard
    )

@main_router.message(LoginStates.phone_number)
async def phone_number(message: types.Message,state: FSMContext):
    user = UserDetail.objects.filter(telegram_id=message.from_user.id).first()
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text

    if user:
        user.phone_number = phone
        user.save()

    await state.clear()

    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Life Gym Saytiga O'tish",
                    url="http://127.0.0.1:8000/ai_app/dashboard/"
                )
            ]
        ]
    )
    await message.answer("Muvaffaqiyatli ro'yxatdan o'tdingiz!", reply_markup=ReplyKeyboardRemove())
    await message.answer("Boshqaruv paneli:", reply_markup=buttons)

