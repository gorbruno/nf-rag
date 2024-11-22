#!/usr/bin/env python
import websockets
from model.client import client
from cache.query.proccessing import load_context, save_context
from cache.query.proccessing import clear_user_context

async def get_model_response(context_db, context_key: str, user_input, max_tokens: int):
    """Запрос к модели"""

    context = await load_context(context_db, context_key, user_input)

    # Сообщения для модели
    messages = [{"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."}]
    messages.extend(context)
    
    # Вызов модели
    response = await client.chat_completion(messages, max_tokens=max_tokens)
    response_content = response['choices'][0]['message']['content']

    await save_context(context_db, context, context_key, response_content)

    return response_content

async def real_time_inference(contex_db, context_key, server_url):
    while True:
        # Запрашиваем ввод пользователя
        user_input = input("User: ")
        if user_input == "exit":
            break
        elif user_input == "clean":
            await clear_user_context(contex_db, context_key)
            print("context cleaned")
            continue

        await ans_receive(server_url, user_input)


# Подключение к серверу и получение ответа
async def ans_receive(server_url, user_input):
    async with websockets.connect(server_url) as websocket:  
        # Отправляем запрос на сервер
        await websocket.send(user_input)
        while True:
            try:
                # Принимаем ответ с сервера с эффектом печати
                while True:
                    char = await websocket.recv()
                    print(char, end='', flush=True)
            except websockets.exceptions.ConnectionClosed:
                #print("Соединение закрыто сервером")
                break
        print() # перенос строки

