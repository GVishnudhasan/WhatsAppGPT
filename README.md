
# WhatsApp Chatbot with OpenAI's GPT-3.5

This is a chatbot application that integrates OpenAI's GPT-3.5 language model with WhatsApp using Twilio's API. The chatbot is designed to provide human-like responses to user queries and engage in natural conversation.


## ChatGPT-WhatsApp Integration
This project integrates OpenAI's ChatGPT model in WhatsApp using Twilio's messaging service.

## Requirements

Python 3.7+

Twilio account

OpenAI API key

## Installation

Clone this repository to your local machine.

Create a virtual environment for the project: `python -m venv venv`.

Install the required packages.

### Create a .env file in the root directory with the following environment variables:

`TWILIO_SID=<your Twilio account SID>`
`TWILIO_TOKEN=<your Twilio auth token>`
`OPENAI_KEY=<your OpenAI API key>`

## Usage
Run the Flask application using the run.py command: `python run.py`.

Send a message to your Twilio phone number and receive an automated response generated by ChatGPT!
Customization

You can customize the behavior of ChatGPT by modifying the `ai_response()` function in `openai_chat/ai_response.py`.

The function takes an input string and returns a string response generated by ChatGPT. You can adjust the various parameters of the openai.Completion.create() method to control the behavior of the model.
