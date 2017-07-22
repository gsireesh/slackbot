from slackclient import SlackClient
from math import log, exp
import time, random

class BotPoster():

    def __init__(self, token, users_to_respond=None, prob_after_24h=0.95):
        self.users = users_to_respond
        self.slack_client = SlackClient(token)
        self.last_posted = None
        self.alpha =  self.calculate_alpha(prob_after_24h)

    def process_message(msg):
        pass

    def should_post(self):
        time_elapsed = time.time() - self.last_posted
        threshold = exp(self.alpha * time_elapsed)
        random_number = random.random()
        return random_number > threshold

    def post_message(self, text, channel):
        self.slack_client.api_call('chat.postMessage', channel=channel, text=text)
        self.last_posted = time.now()

    def calculate_alpha(prob_after_24h)
        return - log(1 - prob_after_24h) / (24 * 60 * 60)

def main():
    pass

if __name__ == '__main__':
    main()