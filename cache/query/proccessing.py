#!/usr/bin/env python
import json

# Загрузить текущий контекст из Redis
async def load_context(db, context_key: str, user_input: str):
    context = await db.get(context_key)
    if context:
        context = json.loads(context)
    else:
        context = []

    context.append({"role": "user", "content": user_input})
    # Сохранить в Redis последние 5 сообщений
    context = context[-5:]
    await db.set(context_key, json.dumps(context))

    return context

# Добавить ответ модели в контекст
async def save_context(db, context: list[dict[str,str]], context_key: str, response: str):
    context.append({"role": "assistant", "content": response})
    # Обновить Redis
    await db.set(context_key, json.dumps(context))

async def clear_user_context(db, context_key: str):
    """Удаление контекста пользователя."""
    await db.delete(context_key)

async def shutdown(db):
    await db.aclose()