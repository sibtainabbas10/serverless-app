from __future__ import print_function

import json
# import jwt

# JWT_EXP_DELTA = 365
# JWT_SECRET = 'BlaBla'
# JWT_ALGO = 'HS256'

def lambda_handler(event, context):
	return "Hello from Lambda!"
    # payload = {
    #     'username': 'sib',
    #     'exp': datetime.utcnow() + timedelta(days=JWT_EXP_DELTA)
    # }
    
    # #Encode the payload 
    # encoded_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)
    # if encoded_token:
    #     response_body = {'token': encoded_token}
    #     return response_body