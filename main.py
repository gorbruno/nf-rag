#!/usr/bin/env python
import asyncio
from service.server import websocket_endpoint
from fastapi import FastAPI, WebSocket
from settings.config import MAIN_SERVER_NAME
import sys
import os
# Добавляем путь проекта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

@app.websocket(f"/{MAIN_SERVER_NAME}")
async def response_ws(websocket: WebSocket):
    await websocket_endpoint(websocket)

