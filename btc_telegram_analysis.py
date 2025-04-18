
import requests
from datetime import datetime
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

def analyze_and_send():
    price = get_btc_price()
    signal = "BUY" if price > 80000 else "WAIT"
    message = f"""📈 BTC DAILY ANALYSIS ({datetime.now().strftime('%Y-%m-%d')})
    
💰 Price: ${price}
📊 Trend: {'Bullish' if signal == 'BUY' else 'Neutral'}
💡 Signal: {signal}

🚨 Alert: {'Price above $90K!' if price >= 90000 else 'No alert today.'}
    """
    send_telegram_message(message)

analyze_and_send()
