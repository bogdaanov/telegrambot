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
qqq_m = InlineKeyboardButton(text='Понедельник', callback_data='day_monday')
qqq_t = InlineKeyboardButton(text='Вторник', callback_data='day_tuesday')
qqq_w = InlineKeyboardButton(text='Среда', callback_data='day_wednesday')
qqq_th = InlineKeyboardButton(text='Четверг', callback_data='day_thursday')
qqq_f = InlineKeyboardButton(text='Пятница', callback_data='day_friday')
qqq_s = InlineKeyboardButton(text='Суббота', callback_data='day_saturday')

back_b = InlineKeyboardButton(text='Назад', callback_data='back')



main_menu.insert(btn_order)
main_menu.insert(btn_support)
main_menu.insert(btn_website)
main_menu.insert(btn_share)

sup_m.insert(but_text)
sup_m.insert(but_call)
sup_m.add(back_b)


cday.insert(qqq_m)
cday.insert(qqq_t)
cday.insert(qqq_w)
cday.insert(qqq_th)
cday.insert(qqq_f)
cday.insert(qqq_s)
cday.add(back_b)