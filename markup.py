from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(row_width=2)
btn_order = InlineKeyboardButton(text='Заказать воду', callback_data='btn_order')
btn_support = InlineKeyboardButton(text='Техподдержка', callback_data='btn_support')
btn_website = InlineKeyboardButton(text='Перейти на сайт', url='https://www.google.com/')
btn_share = InlineKeyboardButton(text='Поделиться', switch_inline_query='Бот для заказа воды')

menu_2 = InlineKeyboardMarkup(row_width=2)
btn2_call = InlineKeyboardButton(text='Написать нам', callback_data='btn2_call')
btn2_text = InlineKeyboardButton(text='Позвонить', callback_data='btn2_text')

main_menu.insert(btn_order)
main_menu.insert(btn_support)
main_menu.insert(btn_website)
main_menu.insert(btn_share)

menu_2.insert(btn2_text)
menu_2.insert(btn2_call)