from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove


# --- Main Menu ---
mainMenu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_phone = KeyboardButton(text="Поделиться контактом", request_contact=True)
mainMenu.add(button_phone)

remove_markup = ReplyKeyboardRemove()
# --- Other Menu ---
# btnInfo = KeyboardButton("Информация")
# btnMoney = KeyboardButton("Курсы валют")
# otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMoney, btnMain)
