from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(row_width=2)
btn_order = InlineKeyboardButton(text='Заказать воду', callback_data='btn_order')
btn_support = InlineKeyboardButton(text='Техподдержка', callback_data='btn_support')
btn_website = InlineKeyboardButton(text='Перейти на сайт', url='https://www.google.com/')
btn_share = InlineKeyboardButton(text='Поделиться', switch_inline_query='Бот для заказа воды')

sup_m = InlineKeyboardMarkup(row_width=2)
but_call = InlineKeyboardButton(text='Позвонить', callback_data='but_call')
but_text = InlineKeyboardButton(text='Задать вопрос менеджеру', callback_data='but_text')


cday = InlineKeyboardMarkup(row_width=2)
ord_m = InlineKeyboardButton(text='Понедельник', callback_data='day_monday')
ord_t = InlineKeyboardButton(text='Вторник', callback_data='day_tuesday')
ord_w = InlineKeyboardButton(text='Среда', callback_data='day_wednesday')
ord_th = InlineKeyboardButton(text='Четверг', callback_data='day_thursday')
ord_f = InlineKeyboardButton(text='Пятница', callback_data='day_friday')
ord_s = InlineKeyboardButton(text='Суббота', callback_data='day_saturday')



main_menu.insert(btn_order)
main_menu.insert(btn_support)
main_menu.insert(btn_website)
main_menu.insert(btn_share)

sup_m.insert(but_text)
sup_m.insert(but_call)


cday.insert(ord_m)
cday.insert(ord_t)
cday.insert(ord_w)
cday.insert(ord_th)
cday.insert(ord_f)
cday.insert(ord_s)
