# 語音即時翻譯字幕工具（部署於 Railway）

## 🚀 功能簡介
- 前端錄音（MediaRecorder API）
- WebSocket 傳音訊給後端
- Whisper 模型語音辨識
- Google 翻譯為繁體中文
- 即時字幕顯示於畫面

## 🔧 如何部署
1. 將此專案上傳至 GitHub
2. 登入 [Railway](https://railway.app/)
3. 點 `New Project > Deploy from GitHub Repo`
4. Railway 自動偵測 Dockerfile 後部署
5. 網址開啟後即可使用

## 📦 Whisper 模型版本
使用 `base` 模型，自動語言辨識，翻譯為 `zh-tw`