import requests

INSTANCE_ID = "instance135357"
TOKEN = "5zono6a0eou0jg2e"
BASE_URL = f"https://api.ultramsg.com/{INSTANCE_ID}/"

def send_message(to, message):
    url = BASE_URL + "messages/chat"
    payload = {
        "token": TOKEN,
        "to": to,
        "body": message
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("✅ Message sent successfully!")
    else:
        print("❌ Error sending message:", response.text)

# Test
send_message("03177782554", "Hello Faiza! This is a test message from UltraMsg 🚀")
