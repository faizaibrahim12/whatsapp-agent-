import streamlit as st
import requests

# UltraMsg credentials
INSTANCE_ID = "instance135357"
TOKEN = "5zono6a0eou0jg2e"
BASE_URL = f"https://api.ultramsg.com/{INSTANCE_ID}/"

# Function to send message
def send_message(to, message):
    url = BASE_URL + "messages/chat"
    payload = {
        "token": TOKEN,
        "to": to,
        "body": message
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return True, "✅ Message sent successfully!"
    else:
        return False, f"❌ Error: {response.text}"

# Streamlit App UI
st.title("📲 WhatsApp Message Sender - UltraMsg")

to = st.text_input("📞 Phone Number (e.g., 923177782554)")
message = st.text_area("💬 Enter your message")

if st.button("🚀 Send WhatsApp Message"):
    if to and message:
        success, result_msg = send_message(to, message)
        if success:
            st.success(result_msg)
        else:
            st.error(result_msg)
    else:
        st.warning("Please fill in both the phone number and message.")
