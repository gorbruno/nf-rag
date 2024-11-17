#!/usr/bin/env python
import asyncio

def get_typing_speed_factor(user_speed: int):
    """Скорость печати ответа"""
    # Секунда/элемент
    typing_speeds = {1: 0.2, 2: 0.15, 3: 0.1, 4: 0.05, 5: 0.02}
    return typing_speeds.get(user_speed, 0.05)  # Стандарно на 4 скорости

async def print_typing_effect(response: str, typing_speed_factor: float, websocket):
    """Отправка текста с эффектом печати по символам"""
    for char in response: 
        await websocket.send_text(char)
        await asyncio.sleep(typing_speed_factor)  # Задержка
        
"""async def print_typing_effect(text: str, typing_speed_factor: float):
    for char in text:
        print(char, end='', flush=True)
        await asyncio.sleep(typing_speed_factor)
    print()  # Сдвиг на линию"""