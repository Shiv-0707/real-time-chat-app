#!/usr/bin/env python3
"""Real-time Chat Application with WebSocket"""
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime
from typing import Set

app = FastAPI(title="Real-time Chat App")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.active_connections: Set[WebSocket] = set()
        self.messages = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.discard(websocket)
    
    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(data)
            except Exception:
                pass
    
    def save_message(self, username: str, message: str):
        msg_obj = {
            "timestamp": datetime.now().isoformat(),
            "username": username,
            "message": message
        }
        self.messages.append(msg_obj)
        return msg_obj

manager = ConnectionManager()

@app.get("/health")
async def health():
    return {"status": "ok", "active_connections": len(manager.active_connections)}

@app.get("/messages")
async def get_messages():
    return {"messages": manager.messages[-50:]}  # Last 50 messages

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    join_message = manager.save_message("system", f"{username} joined the chat")
    await manager.broadcast({"type": "system", "data": join_message})
    
    try:
        while True:
            data = await websocket.receive_text()
            message_obj = manager.save_message(username, data)
            await manager.broadcast({"type": "message", "data": message_obj})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        leave_message = manager.save_message("system", f"{username} left the chat")
        await manager.broadcast({"type": "system", "data": leave_message})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
