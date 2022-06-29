from aiogram import types
from .app import dp, bot
from . import markups
import requests


@dp.message_handler(commands=['start'])
async def get_contact(message: types.Message):
    await message.answer(
        f"Привет {message.from_user.first_name} поделись контактом для того чтобы участвовать в промо акции",
        reply_markup=markups.mainMenu)


@dp.message_handler(commands=['delete'])
async def delete_button(message: types.Message):
    await message.answer('delete', reply_markup=markups.remove_markup)


@dp.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        await message.answer('Вы успешно отправили свой номер', reply_markup=markups.remove_markup)
        global phone
        phone = str(message.contact.phone_number)
        data = requests.post('https://webdevacc.makromarket.uz/api/getTGUserPhone', data={'phone': phone})


@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.answer("Команда не распознана")
