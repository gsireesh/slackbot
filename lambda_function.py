import json
from bot_poster import BotPoster
from credentials import load_credentials

print('Loading function')

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    print("Received event: " + json.dumps(event, indent=2))
    credentials = load_credentials(['bot_token'])
    bot = BotPoster(credentials['bot_token'])

    operation = event['httpMethod']
    if operation == 'POST':
        body = json.loads(event['body'])
        print(body['type'])
        if body['type'] == 'url_verification':
            print(body)
            return respond(False, res={'challenge': body['challenge']})

        bot.process_message(body['event'])
        return respond(False, res='Message Posted!')
    if operation == 'GET':
        return respond(False, 'gotcha.')
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))

if __name__ == '__main__':
    print(respond(False, {'challenge':'ohai'}))