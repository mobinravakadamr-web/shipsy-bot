import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Aapka Telegram Bot Token aur Chat ID
TELEGRAM_BOT_TOKEN = "8654386632:AAHKh05tVVEkjvsA4uHHgyDR6WWBdo5QeK0"
TELEGRAM_CHAT_ID = "6470854341"

def send_telegram_message(message_text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message_text
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

@app.route('/')
def home():
    return "Shipsy Automation Server is Live!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    try:
        if request.method == 'GET':
            # Jab aap browser mein kholenge toh yeh test message bhej dega
            send_telegram_message("🚨 Test Alert: Shipsy Webhook is connected successfully!")
            return "Test message sent to Telegram successfully!", 200
            
        data = request.json
        print("Received Shipsy Data:", data)
        
        alert_text = f"🚨 Shipsy Alert!\nNew Data Received:\n{data}"
        send_telegram_message(alert_text)
        
        return jsonify({"status": "success", "message": "Alert sent to Telegram!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
