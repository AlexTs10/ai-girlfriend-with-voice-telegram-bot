#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from aiogram import Bot, Dispatcher, executor, types 
import openai
import os 

openai.api_key = os.getenv('OPENAI_API_KEY') 
bot = Bot(token= 'xxx')
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('Hello! Im a GPT bot. Ask me something')

@dp.message_handler()
async def gpt(message: types.Message):

    #print(message)    
    #chat_id = message.chat.id
    # Get the 5 latest messages history
    #history = await bot.get_messages(chat_id, limit=5)
    #print(history)

    res = openai.ChatCompletion.create(
       # openai.api_key = os.getenv('OPENAI_API_KEY')
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.text},
        ]
    )
    await message.reply(res['choices'][0]['message']['content'])


if __name__ == '__main__':
    executor.start_polling(dp)
