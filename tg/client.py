#!/usr/bin/env python
from settings.config import BOT_TOKEN
from aiogram import Bot, Dispatcher

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
disp = Dispatcher()
