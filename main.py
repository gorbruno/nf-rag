#!/usr/bin/env python
import asyncio
from fastapi import FastAPI, WebSocket
from service.server import websocket_endpoint
from settings.config import MAIN_SERVER_NAME
from tg.client import bot, disp
from tg import chat  # Ensure handlers are registered
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Aiogram bot...")
    bot_task = asyncio.create_task(disp.start_polling(bot))  # Start bot polling
    try:
        yield  # FastAPI app runs here
    finally:
        print("Shutting down Aiogram bot...")
        bot_task.cancel()  # Stop polling
        await bot.session.close()
        print("Bot session closed!")

app = FastAPI(lifespan=lifespan)

# WebSocket route for server communication
@app.websocket(f"/{MAIN_SERVER_NAME}")
async def response_ws(websocket: WebSocket):
    await websocket_endpoint(websocket)
