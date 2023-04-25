from aiogram import Bot, Dispatcher, executor, types
from someFunktion import *


token_api = 'TOKEN'

bot = Bot(token_api)
dp = Dispatcher(bot)


help_text_command = '''
<em>
***************************************
/start - start the bot
***************************************
/help - list of commands
***************************************
The Caesar cipher is a type of substitution
cipher in which each character in the plaintext
is replaced by a character
some fixed number of positions down the alphabet.
---------------------------------------
/caesar_cipher - encrypts your message using
the Caesar cipher
To use this command, type the command, then
your message, and finally the number of letter
shifts, all separated by spaces
---------------------------------------
/caesar_decipher - decrypts a Caesar cipher
To use this command, type the command, then
the message you want to decrypt, and finally
the number of letter shifts, all separated by spaces
***************************************
The Atbash cipher is a monoalphabetic
substitution cipher formed by taking
the alphabet and mapping it to its reverse.
---------------------------------------
/atbash_cipher - encrypts your message
using the Atbash cipher
To use this command, type the command
followed by your message, all separated
by a space
---------------------------------------
/atbash_decipher - decrypts a message
encrypted using the Atbash cipher
To use this command, type the command
followed by the message you want to
decrypt, all separated by a space
***************************************
</em>
'''


@dp.message_handler(commands=['start'])
async def help_comand(message: types.Message ):
    await message.answer(text='Welcome in my Telegram bot')
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_comand(message: types.Message ):
    await message.answer(text=help_text_command, parse_mode='HTML')


all_comand = ['/caesar_cipher', '/caesar_decipher', '/atbash_cipher', '/atbash_decipher']

@dp.message_handler()
async def echo(message: types.Message):
    global all_comand
    text = message.text.split()
    comand = text[0]
    if comand not in all_comand or len(message.text.split()) == 1:
        await message.answer('uncorected input')
        await message.delete()
    else:
        if comand in ['/caesar_cipher', '/caesar_decipher']:
            txt_maess = ' '.join(text[1:-1])
            shift_number = text[-1]
            if comand == '/caesar_cipher':
                if shift_number.isdigit():
                    shift_number = int(shift_number)
                    await message.answer(text=caesar_cipher(txt_maess, shift_number))
                else:
                    await message.answer('uncorected input')
                    await message.delete()
                    return
            else:
                if shift_number.isdigit():
                    shift_number = int(shift_number)
                    await message.answer(text=caesar_decipher(txt_maess, shift_number))
                else:
                    await message.answer('uncorected input')
                    await message.delete()
                    return


        elif comand in ['/atbash_cipher', '/atbash_decipher']:
            txt_maess = ' '.join(text[1:])
            if comand == '/atbash_cipher':
                await message.answer(text=atbash_cipher(txt_maess))
            else:
                await message.answer(text=atbash_decipher(txt_maess))


if __name__ == '__main__':
    executor.start_polling(dp)



