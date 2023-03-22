from flask import Flask, request
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from .openai_chat.ai_response import ai_response
load_dotenv()

sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

app = Flask(__name__)
client = Client(sid, auth_token)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)


@app.route("/")
def home():
    return "Hello, World!"

@app.route("/message", methods=["POST"])
def reply():
    message = request.form.get("body").lower()
    response = ai_response(message)
    return respond(response)