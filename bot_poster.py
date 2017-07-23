from slackclient import SlackClient
from math import log, exp
import time, random, json


class BotPoster():

    def __init__(self, token, users_to_respond=None, prob_after_24h=0.95):
        self.users = users_to_respond
        self.slack_client = SlackClient(token)
        self.last_posted = None
        self.alpha =  self.calculate_alpha(prob_after_24h)

    def process_message(self, msg):
        if True and self.message_meets_criteria(msg): # this should be transitioned to should_post()
            self.post_message('Slack me daddy :sunglasses:', msg['channel'])


    def message_meets_criteria(self, msg):
        print(msg)
        correct_content = 'slack' in msg['text']
        correct_sender = msg['user'] in self.users_to_respond if self.users else True
        return correct_sender and correct_content

    def should_post(self, message_time):
        time_elapsed = message_time - self.last_posted
        threshold = exp(self.alpha * time_elapsed)
        random_number = random.random()
        return random_number > threshold

    def post_message(self, text, channel):
        result = self.slack_client.api_call('chat.postMessage', channel=channel, text=text)
        self.last_posted = time.time()

    def calculate_alpha(self, prob_after_24h):
        return - log(1 - prob_after_24h) / (24 * 60 * 60)