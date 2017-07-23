from flask import Flask, request
from credentials import load_credentials
from bot_poster import BotPoster

app = Flask(__name__)
credentials = load_credentials(['bot_token'], 'credentials.json')
bot = BotPoster(credentials['bot_token'])

@app.route('/message', methods=['POST'])
def respond_to_message():
    body = request.get_json()
    bot.process_message(body)
    return 'Message posted!'


app.run()