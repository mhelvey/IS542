#!/usr/bin/env python3
# Using OAuth1Session
from requests_oauthlib import OAuth1Session


key = 'rZbruFpZPtMAEMAKeF'
secret = 'nMJSAk7teXEMgKaDtUSAf9bBwZFKprFV'

# OAuth endpoints given in the Bitbucket API documentation
request_token_url = 'https://bitbucket.org/!api/1.0/oauth/request_token'
authorization_base_url = 'https://bitbucket.org/!api/1.0/oauth/authenticate'
access_token_url = 'https://bitbucket.org/!api/1.0/oauth/access_token'

bitbucket = OAuth1Session(key, client_secret=secret,
        callback_uri='http://localhost:8000/homepage')
print('Request Token: ', bitbucket.fetch_request_token(request_token_url), '\n')

authorization_url = bitbucket.authorization_url(authorization_base_url)
print('Authorization URL (Please go here and authorize): ', authorization_url, '\n')

redirect_response = input('Paste the full redirect URL here:')
print('Redirect Response: ', bitbucket.parse_authorization_response(redirect_response), '\n')

print('Access Token: ', bitbucket.fetch_access_token(access_token_url), '\n')

r = bitbucket.get('https://bitbucket.org/api/1.0/user\n')
print('User Object Information: ', r.content)




