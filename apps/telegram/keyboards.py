from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_buttons = [
    KeyboardButton('Добавить фото'),
    KeyboardButton('Комплемент'),
    KeyboardButton('Получить фото'),
    KeyboardButton('Отправить локацию', request_location=True)
]
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)