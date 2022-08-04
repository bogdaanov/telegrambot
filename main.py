import logging
from aiogram import Bot, Dispatcher, executor, types
from payments import pay_token, prices
from aiogram.types import PreCheckoutQuery
from aiogram.types.message import ContentTypes
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db import Database
import markup as nav

TOKEN = '5445100027:AAFhMIt7kM8Y7-Ux7OqnI_HEwwRgetwJwCc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')
admin_chat_id = 598265847
storage = MemoryStorage()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Добрый день! Выберите, что хотите сделать',
                               reply_markup=nav.main_menu)

# @dp.message_handler()
# async def unknown (message: types.Message):
#     if message.chat.type == 'private':
#         await bot.send_message(message.from_user.id, 'Я вас не понимаю, нажмите /start, чтобы начать')

#Рассылка
@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_chat_id:
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

#Техподдержка
@dp.callback_query_handler(text_startswith='but')
async def supp(call: types.CallbackQuery):
    if call.data == 'but_call':
        await bot.send_message(call.from_user.id, 'Номер для связи +380930365611', reply_markup=nav.sup_m)
    elif call.data == 'but_text':
        await bot.send_message(call.from_user.id, 'Напишите ваш вопрос',)



@dp.message_handler()
async def message_to_admin(message: types.Message):
    if message.reply_to_message == None:
        await bot.forward_message(admin_chat_id, message.from_user.id, message.message_id)
    else:
        if message['from'].id == admin_chat_id:
            if message.reply_to_message.forward_from.id:
                await bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            pass


@dp.callback_query_handler(text_startswith='btn')
async def shop(call: types.CallbackQuery):
    if call.data == 'btn_order':
        await bot.send_message(call.from_user.id, 'Выберите день доставки', reply_markup=nav.cday)
    elif call.data == 'btn_support':
        await bot.send_message(call.from_user.id, 'Выберите как хотите связаться', reply_markup=nav.sup_m)

@dp.callback_query_handler(text_startswith='day')
async def buy(call: types.CallbackQuery):
    if call.data[:3] == 'day':
        await bot.send_invoice(call.from_user.id, title='Вода', description='Вкусная вода))', provider_token=pay_token,
                               currency='uah', need_phone_number=True, need_shipping_address=True,
                               prices=prices, start_parameter='example', payload='some_invoice')

@dp.shipping_query_handler(lambda query: True)
async def shipping(shipping_query: types.ShippingQuery):
    await bot.answer_shipping_query(shipping_query.id, ok=True)

@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    await bot.send_message(message.chat.id, 'Успешная оплата')

@dp.callback_query_handler(text='back')
async def back_button(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, 'Назад', reply_markup=nav.main_menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)