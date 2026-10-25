
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Shipsy Bot is Running Successfully!"

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get("Body")
    print(f"Message mila: {incoming_msg}")
    # Yahan Shipsy automation aur WhatsApp reply ka logic aayega
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
  
