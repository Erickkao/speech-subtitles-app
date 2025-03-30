import io
import wave
import tempfile
import base64
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import whisper
from googletrans import Translator

# 初始化應用程式
app = FastAPI()

# 掛載前端靜態檔案（frontend 資料夾）
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# 啟用 CORS 讓前端能存取 API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化 Whisper 模型與翻譯器
model = whisper.load_model("base")
translator = Translator()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    buffer = b""
    try:
        while True:
            data = await websocket.receive_bytes()
            buffer += data
            if len(buffer) > 32000:  # 約 2 秒音訊
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
                    with wave.open(tmpfile.name, "wb") as wf:
                        wf.setnchannels(1)
                        wf.setsampwidth(2)
                        wf.setframerate(16000)
                        wf.writeframes(buffer)
                    buffer = b""

                    result = model.transcribe(tmpfile.name)
                    text = result["text"]
                    translated = translator.translate(text, dest="zh-tw").text
                    await websocket.send_text(translated)
    except Exception as e:
        print("WebSocket closed:", e)
