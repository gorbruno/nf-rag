#!/usr/bin/env python
import redis.asyncio as aioredis
from settings.config import REDIS_HOST, REDIS_PORT, REDIS_CONTEXT_PREFIX, USER_ID

# Подключение к Redis
redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")

# Ключ для хранения контекста пользователя
context_key = f"{REDIS_CONTEXT_PREFIX}{USER_ID}"