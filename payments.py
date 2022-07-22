#portmone

from aiogram import types
from aiogram.types import LabeledPrice

pay_token = '1661751239:TEST:598265847'

prices = [LabeledPrice(label='товар 1', amount=1000)]
shipping_method = types.ShippingOption(id='courier', title='Привезем по укзанному адресу').add(types.LabeledPrice('Доставка', 10))

