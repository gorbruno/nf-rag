#!/usr/bin/env python
from settings.appearance import print_typing_effect, get_typing_speed_factor
from model.chat import get_model_response
from cache.query.db import redis, context_key
from settings.config import MAX_TOKENS, TYPING_SPEED, MAIN_SERVER_NAME, MAIN_SERVER_HOST, MAIN_SERVER_PORT

response_url = f"ws://{MAIN_SERVER_HOST}:{MAIN_SERVER_PORT}/{MAIN_SERVER_NAME}"

async def websocket_endpoint(websocket):
    await websocket.accept()

    data = await websocket.receive_text()

    response = await get_model_response(context_key=context_key,context_db=redis, user_input=data, max_tokens=MAX_TOKENS)

    typing_speed_factor = get_typing_speed_factor(TYPING_SPEED)

    await print_typing_effect(response, typing_speed_factor, websocket)
    
    # Закрытие сессии
    await websocket.close()