from twilio.rest import Client

# Twilio credentials
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
client = Client(account_sid, auth_token)

# WhatsApp message details
from_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox number
to_whatsapp_number = 'whatsapp:+918072990775'   # Your verified phone number

message_body = "🩸 URGENT: A hospital near you needs B+ blood . Can you donate? Reply 'Available' or 'Not Available'."

# Send message
message = client.messages.create(
    body=message_body,
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(f"Message sent! SID: {message.sid}")