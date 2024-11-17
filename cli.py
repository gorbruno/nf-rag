#!/usr/bin/env python
import asyncio
from cache.query.proccessing import shutdown
from cache.query.db import redis, context_key
from service.server import response_url
from model.chat import real_time_inference

async def communicate_with_server():
    try:
        await real_time_inference(contex_db=redis, context_key=context_key, server_url=response_url)
    finally:
        # Завершение работы с Redis
        await shutdown(redis)

# Запуск асинхронного процесса общения с сервером
asyncio.run(communicate_with_server())
