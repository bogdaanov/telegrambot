import logging
from aiogram import Bot, Dispatcher, executor, types
from payments import pay_token, prices
from aiogram.types import PreCheckoutQuery

from db import Database
import markup as nav

TOKEN = '5445100027:AAFhMIt7kM8Y7-Ux7OqnI_HEwwRgetwJwCc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Добрый день! Выберите, что хотите сделать',
                               reply_markup=nav.main_menu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, 'Я Вас не понимаю. Нажмите /start, чтобы начать')

@dp.callback_query_handler(text_startswith='btn')
async def shop(call: types.CallbackQuery):
    if call.data == 'btn_order':
        await bot.send_message(call.from_user.id, 'Выберите день доставки', reply_markup=nav.cday)
    elif call.data == 'btn_support':
        await bot.send_message(call.from_user.id, 'Выберите как хотите связаться', reply_markup=nav.sup_m)

@dp.callback_query_handler(text_startswith='qqq')
async def buy(call: types.CallbackQuery):
    if call.data == 'day':
        await bot.send_invoice(call.from_user.id, title='Вода', description='Вкусная вода))', provider_token=pay_token,
                               currency='uah', need_phone_number=True, need_shipping_address=True,
                               prices=prices, start_parameter='example', payload='some_invoice')


@dp.pre_checkout_query_handler(lambda q: True)
async def checkout(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

#Техподдеержка
@dp.callback_query_handler(text_startswith='but')
async def supp(call: types.CallbackQuery):
    if call.data == 'but_call':
        await bot.send_message(call.from_user.id, 'Номер для связи +38********', reply_markup=nav.sup_m)
    elif call.data == 'but_text':
        await bot.send_message(call.from_user.id, 'Вопрос: ', reply_markup=nav.sup_m)


#Рассылка
@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 598265847:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0],0)

            await bot.send_message(message.from_user.id, 'Успешно отправлено')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)