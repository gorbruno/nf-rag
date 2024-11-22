#!/usr/bin/env python
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# HF параметры
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL = os.getenv("MODEL")
# Настройки инференса
TYPING_SPEED = int(os.getenv("TYPING_SPEED")) # 5
MAX_TOKENS = int(os.getenv("MAX_TOKENS")) # 1000
# Настройки Redis
REDDIS_SERVER_NAME = os.getenv("REDDIS_SERVER_NAME")
REDIS_HOST =  os.getenv("REDIS_HOST") # 'localhost'
REDIS_PORT = int(os.getenv("REDIS_PORT")) # 6379
REDIS_CONTEXT_PREFIX = "user_context:"  # Префикс для хранения данных пользователей
USER_ID = os.getenv("USER_ID")

MAIN_SERVER_NAME = os.getenv("MAIN_SERVER_NAME")
MAIN_SERVER_HOST = os.getenv("MAIN_SERVER_HOST")
MAIN_SERVER_PORT = os.getenv("MAIN_SERVER_PORT")

CHROMADB_SERVER_NAME = os.getenv("CHROMADB_SERVER_NAME")

BOT_TOKEN = os.getenv("BOT_TOKEN")