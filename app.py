import requests
from flask import Flask
import threading
import time

app = Flask(__name__)

TOKEN = "你的TOKEN"
CHAT_ID = "你的ID"

last_signal = None

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": msg})

def get_price():
    return 12  # 后面再换真实数据

def check():
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

    return price, signal

# 👇 后台循环（自动运行）
def loop():
    while True:
        check()
        time.sleep(300)

# 👇 网页显示（解决空白）
@app.route("/")
def home():
    price, signal = check()
    return f"""
    <h1>🐷 猪周期系统</h1>
    <p>当前猪价：{price}</p>
    <p>当前信号：{signal}</p>
    """

# 启动后台线程
threading.Thread(target=loop).start()

app.run(host="0.0.0.0", port=10000)
