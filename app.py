import requests
from flask import Flask, jsonify

app = Flask(__name__)
last_signal = None

TOKEN = "你的TOKEN"
CHAT_ID = "你的ID"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": msg})

def get_price():
    return 12  # 先用固定值，后面再升级

@app.route("/")
def run():
    global last_signal

    price = get_price()

    if price <= 13:
        signal = "🟢 买入"
    elif price > 18:
        signal = "🔴 卖出"
    else:
        signal = "⚫ 观望"

    if signal != last_signal:
        send(f"猪周期信号：{signal}")
        last_signal = signal

    return {"price": price, "signal": signal}

app.run(host="0.0.0.0", port=10000)
