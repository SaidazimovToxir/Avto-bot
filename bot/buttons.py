from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class BotButtons:
    @staticmethod
    def create_contact_btn():
        return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Kontakni yuborish", request_contact=True))

    @staticmethod
    def create_main_btn():
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("Aloqa 📲"),
            KeyboardButton("Xizmatlar ⚒"),
            KeyboardButton("Joylashuv 📍")
        )

    @staticmethod
    def create_service_btn():
        return ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton("Polirofka"),
            KeyboardButton("Plyonka"),
            KeyboardButton("Ximchistka"),
            KeyboardButton("Tanirovka"),
            KeyboardButton("Orqaga")
        )

    @staticmethod
    def create_back_btn():
        return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Orqaga'))

    @staticmethod
    def create_inline_keys():
        return InlineKeyboardMarkup(row_width=2).add(
            InlineKeyboardButton(text='Aloqa 📲', callback_data='contact_aloqa'),
            InlineKeyboardButton(text='Joylashuv 📍', callback_data='location')
        )

contact_btn = BotButtons.create_contact_btn()
main_btn = BotButtons.create_main_btn()
service_btn = BotButtons.create_service_btn()
back_btn = BotButtons.create_back_btn()
inline_keys = BotButtons.create_inline_keys()
