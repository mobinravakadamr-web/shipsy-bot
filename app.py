from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Shipsy Automation Bot is Live and Ready!"

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")
    print(f"Message mila: {incoming_msg} (Sender: {sender})")
    
    # Yahan hum Shipsy data aur WhatsApp reply ka logic aage jurenge
    return "<Response><Message>Message mil gaya hai!</Message></Response>", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
