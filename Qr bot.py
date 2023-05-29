from aiogram import Bot, Dispatcher, types, executor
import pyqrcode as pq
import os

bot = Bot(token='6082663790:AAEqFqwLSIl3kqEZ12d0SFMCqEuIZBoDBs4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hello! Send me a message and I'll generate a QR code for you.")

@dp.message_handler()
async def send_text_based_qr(message: types.Message):
    await message.reply('put qrcode!\nplease wait')

    qr_code = pq.create(message.text)
    qr_code.png('code.png', scale=6)

    with open('code.png', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)
        await bot.send_message (message.chat.id, 'jreijcorih3cuhrucrichu4iru!')
        os.unlink()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)