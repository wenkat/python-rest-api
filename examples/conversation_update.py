#!/usr/bin/env python
import argparse
import messagebird

parser = argparse.ArgumentParser()
parser.add_argument('--accessKey', help='access key for MessageBird API', type=str, required=True)
parser.add_argument('--conversationId', help='conversation ID that you want to update', type=str, required=True)
args = vars(parser.parse_args())

try:
    client = messagebird.Client(args['accessKey'])

    conversation = client.conversation_update(args['conversationId'], {'status': 'active'})

    # Print the object information.
    print('The following information was returned as a Conversation object:')
    print(conversation)

except messagebird.client.ErrorException as e:
    print('An error occured while requesting a Conversation object:')

    for error in e.errors:
        print('  code        : %d' % error.code)
        print('  description : %s' % error.description)
        print('  parameter   : %s\n' % error.parameter)
