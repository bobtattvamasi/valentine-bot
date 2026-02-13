import json
import os
from http.server import BaseHTTPRequestHandler

import httpx

TELEGRAM_API_BASE = "https://api.telegram.org/bot{token}/{method}"


def telegram_send_message(token: str, chat_id: int, text: str, webapp_url: str | None = None) -> None:
    payload: dict = {"chat_id": chat_id, "text": text}

    if webapp_url:
        payload["reply_markup"] = {
            "inline_keyboard": [
                [
                    {
                        "text": "Открой валентинку 💝",
                        "web_app": {"url": webapp_url},
                    }
                ]
            ]
        }

    url = TELEGRAM_API_BASE.format(token=token, method="sendMessage")
    with httpx.Client(timeout=10.0) as client:
        response = client.post(url, json=payload)
        response.raise_for_status()


class handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True, "service": "telegram-webhook"}).encode("utf-8"))

    def do_POST(self) -> None:
        token = os.environ.get("BOT_TOKEN")
        webapp_url = os.environ.get("WEBAPP_URL")

        if not token:
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": False, "error": "BOT_TOKEN is not set"}).encode("utf-8"))
            return

        content_length = int(self.headers.get("content-length", "0"))
        raw_body = self.rfile.read(content_length) if content_length > 0 else b"{}"

        try:
            update = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": False, "error": "invalid json"}).encode("utf-8"))
            return

        message = update.get("message") or {}
        chat = message.get("chat") or {}
        text = (message.get("text") or "").strip()
        chat_id = chat.get("id")

        if text == "/start" and chat_id is not None:
            try:
                telegram_send_message(
                    token=token,
                    chat_id=chat_id,
                    text="💕 Привет, моя любимая! У меня есть для тебя сюрприз...",
                    webapp_url=webapp_url,
                )
            except httpx.HTTPError:
                self.send_response(502)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"ok": False, "error": "telegram api request failed"}).encode("utf-8"))
                return

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True}).encode("utf-8"))
