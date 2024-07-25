import uvicorn
from fastapi import FastAPI

import socketio

app = FastAPI()

sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
combined_app = socketio.ASGIApp(sio, app)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@sio.on("connect")
async def connect(sid, env):
    print(f"New Client Connected to This id : {sid}")


@sio.on("disconnect")
async def disconnect(sid):
    print(f"Client Disconnected: {sid}")


if __name__=="__main__":
    uvicorn.run("app:combined_app", host="0.0.0.0", port=4000, lifespan="on", reload=True)