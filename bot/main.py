import logging
import telebot
from buttons import contact_btn, main_btn, service_btn, back_btn, inline_keys
from api import create_user, create_feedback

class AutoBot:
    def __init__(self, api_token):
        self.API_TOKEN = api_token
        self.bot = telebot.TeleBot(api_token)
        logging.basicConfig(level=logging.INFO)

        self.bot.message_handler(commands=['start'])(self.get_contact)
        self.bot.message_handler(content_types=['contact'])(self.contact_received)
        self.bot.message_handler(func=lambda message: message.text == 'Joylashuv 📍')(self.response_location_btn)
        self.bot.message_handler(func=lambda message: message.text == 'Aloqa 📲')(self.response_contact_btn)
        self.bot.message_handler(func=lambda message: message.text == 'Xizmatlar ⚒')(self.response_service_btn)
        self.bot.message_handler(func=lambda message: message.text == 'Polirofka')(self.service_btn_in_polirofki)
        self.bot.message_handler(func=lambda message: message.text == 'Plyonka')(self.service_btn_in_plyonki)
        self.bot.message_handler(func=lambda message: message.text == 'Ximchistka')(self.service_btn_in_ximchistki)
        self.bot.message_handler(func=lambda message: message.text == 'Tanirovka')(self.service_btn_in_tanirovki)
        self.bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'contact_aloqa')(self.polirofki_contact)
        self.bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'location')(self.polirofki_location)
        self.bot.message_handler(func=lambda message: message.text == 'Orqaga')(self.service_btn_in_back)

    def run(self):
        if __name__ == '__main__':
            print("Bot polling...")
            self.bot.polling(none_stop=True)

    def get_contact(self, message):
        self.bot.send_message(message.chat.id, "Iltimos, Botdan to'liq foydalanish uchun telefon raqamingizni kiriting ☎️", reply_markup=contact_btn)

    def contact_received(self, message):
        print(create_user(message.from_user.username, message.from_user.first_name, message.from_user.id, message.contact.phone_number))
        self.bot.send_message(message.chat.id, f'Assalomu alaykum hurmatli <b>{message.from_user.first_name}</b>\nBizning Avto-Botimizga xush kelibsiz', reply_markup=main_btn, parse_mode='HTML')

    def response_location_btn(self, message):
        self.bot.send_message(message.chat.id, "Manzilni bilish uchun ustiga bosing.")
        self.bot.send_location(message.chat.id, 41.336565, 69.209774, reply_markup=back_btn)

    def response_contact_btn(self, message):
        self.bot.send_message(message.chat.id, "Biz bilan bog'lanish uchun quyidagi telefon raqamiga qo'ng'iroq qiling. 📱", reply_markup=back_btn)
        self.bot.send_contact(message.chat.id, "+998983049282", "Avto")
        self.bot.send_contact(message.chat.id, "+998901349282", "Avto 2")

    def response_service_btn(self, message):
        self.bot.send_message(message.chat.id, "Bizning xizmatlar: ⚙️", reply_markup=service_btn)

    def service_btn_in_polirofki(self, message):
        photo_path = 'tanirovka.jpg'
        photo_caption = """
        Palirovka o’zi nima uchun kerak?

        Yangi mashinani ham palirovka qilish kerakmi?

        Albatta, qilish kerak.

        Chunki, yangi mashinalada ham galagramma bo’ladi.

        Palirovka xizmatimiz o’ziga xos texnologiya asosida, lak qatlamiga ziyon yetkazilmasdan qilinadi.

        Auto Effect har doim sizga sifatli xizmat ko’rsatishga tayyor.

        Sifatli xizmat va hadiyalar ulashamiz

        <a href="https://t.me/tox_uzb">Telegram</a> | <a href="https://instagram.com/12345678">Instagram</a> | <a href="https://youtube.com/">YouTube</a>
        """  # Video tavsifi
        self.bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=photo_caption, reply_markup=inline_keys, parse_mode='HTML')

    def service_btn_in_plyonki(self, message):
        photo_path = 'tanirovka.jpg'
        photo_caption = """
        🥇Poluritan plyonkamiz 
        🛡2 yil Kafolat
        ♻️O'zini o'zi tiklaydi
        💎Kuzovdan ajralib qomidi
        💦Gidrafob xsusiyati bor
        ⚠️Rangini o'zgartrmaydi.

        <a href="https://t.me/tox_uzb">Telegram</a> | <a href="https://instagram.com/12345678">Instagram</a> | <a href="https://youtube.com/">YouTube</a>

        """
        self.bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=photo_caption, reply_markup=inline_keys, parse_mode='HTML')

    def service_btn_in_ximchistki(self, message):
        photo_path = 'tanirovka.jpg'
        photo_caption = """
        Assalomu alaykum !

        <a href="https://t.me/tox_uzb">Telegram</a> | <a href="https://instagram.com/12345678">Instagram</a> | <a href="https://youtube.com/">YouTube</a>
        """
        self.bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=photo_caption, reply_markup=inline_keys, parse_mode='HTML')

    def service_btn_in_tanirovki(self, message):
        photo_path = 'tanirovka.jpg'
        photo_caption = """
        Tonirovkalarning nima farqlari bor deb juda yam koʻp savollar beriladi, bularni farqi ishlab chiqaruvchi tomonidan beriladigan kafolat. Eng asosiy farqlaridan bizning iqlim isib borayotganini hisobga olsak oʻzida 65% issiqni ushlab qoladi 100% ultrafioletni qaytaradi.

        Premium tonirovka xizmatlari kerak boʻlsa bizga murojaat qiling.

        Yuqori sifat oʻzgacha hissiyot 🔥

        <a href="https://t.me/tox_uzb">Telegram</a> | <a href="https://instagram.com/12345678">Instagram</a> | <a href="https://youtube.com/">YouTube</a>
        """
        self.bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=photo_caption, reply_markup=inline_keys, parse_mode='HTML')

    def polirofki_contact(self, callback_query):
        self.bot.send_message(callback_query.message.chat.id, "Bog'lanish uchun Kontaktlar: ")
        self.bot.send_contact(callback_query.message.chat.id, "+998983049282", "Avto 1")
        self.bot.send_contact(callback_query.message.chat.id, "+998901349282", "Avto 3")

    def polirofki_location(self, callback_query):
        self.bot.send_message(callback_query.message.chat.id, "Joylashuvni olish uchun bosing: ")
        self.bot.send_location(callback_query.message.chat.id, 41.336565, 69.209774)

    def service_btn_in_back(self, message):
        self.bot.send_message(message.chat.id, "Siz bosh menyuga qaytdingiz. ⛓", reply_markup=main_btn)


if __name__ == '__main__':
    bot = AutoBot('6813872076:AAFhfAmAY2f4LjNn5rCwZaBIKZHxCyr-AX0')
    bot.run()