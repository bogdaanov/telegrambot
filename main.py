import logging
from aiogram import Bot, Dispatcher, executor, types

import markup as nav

TOKEN = '5445100027:AAFhMIt7kM8Y7-Ux7OqnI_HEwwRgetwJwCc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Добрый день! Выберите, что хотите сделать', reply_markup=nav.main_menu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Я Вас не понимаю. Нажмите /start, чтобы начать')

@dp.callback_query_handler(text_contains='btn')
async def shop(call: types.CallbackQuery):
    if call.data == 'btn_order':
        await bot.send_message(call.from_user.id, 'OK', reply_markup=nav.main_menu)
    elif call.data == 'btn_support':
        await bot.send_message(call.from_user.id, 'Выберите как хотите связаться', reply_markup=nav.menu_2)

@dp.callback_query_handler(text_contains='btn2')
async def supp(call: types.CallbackQuery):
    if call.data == 'btn2_call':
        await bot.send_message(call.from_user.id, 'Номер для связи +38********', reply_markup=nav.menu_2)
    elif call.data == 'btn2_text':
        await bot.send_message(call.from_user.id, 'ffff', reply_markup=nav.menu_2)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)