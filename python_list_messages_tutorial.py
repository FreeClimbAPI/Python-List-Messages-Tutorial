from __future__ import print_function
import time
import freeclimb
import os

configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = os.environ['ACCOUNT_ID']
configuration.password = os.environ['AUTH_TOKEN']

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"
# Create an instance of the API class
api_instance = freeclimb.DefaultApi(freeclimb.ApiClient(configuration))

message_list = api_instance.list_sms_messages(configuration.username)

print(message_list)
