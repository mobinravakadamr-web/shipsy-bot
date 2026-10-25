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
    # Jaise hi aap browser mein yeh link kholenge, Telegram par test message aur notification aa jayegi
    send_telegram_message("🚨 Shipsy Automation: Server is live and ready for Excel data!")
    return "Shipsy Automation Bot is Live and Ready!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    try:
        if request.method == 'GET':
            send_telegram_message("📊 Excel sheet request received via browser link!")
            return "Excel request processed!", 200
            
        data = request.json
        print("Received Data:", data)
        
        alert_text = f"📁 Shipsy Excel Update:\n{data}"
        send_telegram_message(alert_text)
        
        return jsonify({"status": "success", "message": "Sent to Telegram!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
