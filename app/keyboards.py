from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_mechanics, get_services

contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить контакт', request_contact=True)]
], resize_keyboard=True, input_field_placeholder='Нажмите кнопку ниже.')




main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Записаться на ТО')],
    [KeyboardButton(text='Контакты/локация')]
], resize_keyboard=True)


async def mechanics():
    all_mechanics = await get_mechanics()
    keyboard = InlineKeyboardBuilder()
    for mechanic in all_mechanics:
        keyboard.add(InlineKeyboardButton(text=mechanic.name, callback_data=f'mechanic_{mechanic.id}'))
    return keyboard.adjust(1).as_markup()


async def services():
    all_services = await get_services()
    keyboard = InlineKeyboardBuilder()
    for service in all_services:
        keyboard.add(InlineKeyboardButton(text=service.name, callback_data=f'service_{service.id}'))
    return keyboard.adjust(1).as_markup()