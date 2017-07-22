from slackclient import SlackClient
import math

class BotPoster():

    def __init__(self, token, users_to_respond=None):
        self.users = users_to_respond
        self.slack_client = SlackClient(token)

    def process_message(msg):
        pass

    def should_post(self):
        return True

    def post_message(self, text, channel):
        self.slack_client.api_call('chat.postMessage', channel=channel, text=text)


def main():
    pass

if __name__ == '__main__':
    main()