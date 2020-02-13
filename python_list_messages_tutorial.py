import freeclimb
import os
import requests

configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = os.environ['ACCOUNT_ID']
configuration.password = os.environ['AUTH_TOKEN']

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"
# Create an instance of the API class
api_instance = freeclimb.DefaultApi(freeclimb.ApiClient(configuration))

first_message = api_instance.list_sms_messages(configuration.username)

next_page_uri = first_message.next_page_uri

file = open("message_results.txt", "w")
file.write(str(first_message.messages))

while(next_page_uri != None):
    next_message = requests.get(url=configuration.host + next_page_uri, auth=(configuration.username, configuration.password))
    file.write('\n')
    file.write(str(next_message.json().get('messages')))
    next_page_uri = next_message.json().get('next_page_uri')

file.close()
