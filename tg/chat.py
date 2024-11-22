#!/usr/bin/env python
from tg.client import disp
from model.chat import get_model_response
from cache.query.db import redis, context_key
from cache.query.proccessing import clear_user_context
from aiogram.types import Message
#from aiogram.utils import executor
from aiogram.filters import Command
from settings.config import BOT_TOKEN, MAX_TOKENS

# Handle commands (e.g., /start)
@disp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.reply("Hello! Send me any message, and I'll respond!")

@disp.message(Command(commands=['clean']))
async def clean_command(message: Message):
    await clear_user_context(redis, context_key)
    await message.reply("Context cleaned!")

# Handle all text messages (no tags required)
@disp.message()
async def handle_message(message: Message):
    user_input = message.text
    response = await get_model_response(context_key=context_key, context_db=redis,
                                  user_input=user_input, max_tokens=MAX_TOKENS)
    
    await send_large_message(message, response)

async def send_large_message(message: Message, text: str):
    # Telegram's message limit is 4096 characters
    max_length = 4096

    # Split the message into smaller parts if necessary
    while len(text) > max_length:
        await message.answer(text[:max_length])
        text = text[max_length:]

    # Send the remaining part
    await message.answer(text)