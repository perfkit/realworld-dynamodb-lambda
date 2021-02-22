import logging
import re
import requests

BENCHMARK_CONFIG = """
event_processing:
  description: Real world DynamoDB Benchmark for AWS Lambda.
  provider: aws
  region: us-east-1
  stage: dev
"""


# Util

def getEndpointURL(spec, postfix):
    return f"https://{spec['endpoint']}/{spec['stage']}/api/{postfix}"


# Endpoints:
#
# POST -   https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/users
# POST -   https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/users/login
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/user
# PUT -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/user
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/profiles/{username}
# POST -   https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/profiles/{username}/follow
# DELETE - https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/profiles/{username}/follow
# POST -   https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}
# PUT -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}
# DELETE - https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}
# POST -   https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}/favorite
# DELETE - https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}/favorite
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/feed
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/tags
# POST -   https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}/comments
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}/comments
# DELETE - https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/articles/{slug}/comments/{id}
# GET -    https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/ping
# DELETE - https://<ENDPOINT_ID>.execute-api.us-east-1.amazonaws.com/dev/api/__TESTUTILS__/purge

# User API

def createUser(spec, username, password, email):
    data = {
        'user': {
            'username': username,
            'password': password,
            'email': email
        }
    }
    resp = requests.post(url=getEndpointURL(spec, "users"), json=data)
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def loginUser(spec, email, password):
    data = {
        'user': {
            'password': password,
            'email': email
        }
    }
    resp = requests.post(url=getEndpointURL(spec, "users/login"), json=data)
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def getUser(spec, token):
    resp = requests.get(url=getEndpointURL(spec, "user"), headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def updateUser(spec, token, config):
    data = {
        'user': config      # config can contain: { 'password': password, 'email': email, 'image': image, 'bio': bio }
    }
    resp = requests.put(url=getEndpointURL(spec, "user"), json=data, headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")

def getProfile(spec, token, username):
    resp = requests.get(url=getEndpointURL(spec, f"profiles/{username}"), headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")

def followUser(spec, token, username):
    data = {}
    resp = requests.post(url=getEndpointURL(spec, f"profiles/{username}/follow"), json=data, headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")

def unfollowUser(spec, token, username):
    data = {}
    resp = requests.delete(url=getEndpointURL(spec, f"profiles/{username}/follow"), json=data, headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")

# Articles API

# TODO

# SB entry points

def prepare(spec):
    log = spec.run(f"serverless deploy --stage {spec['stage']} --region {spec['region']}", image='serverless_cli')
    spec['endpoint'] = re.match(r"https://([\w.]+)/", log).group(1)
    logging.info(f"service endpoint={spec['endpoint']}")


def invoke(spec):
    createUser(spec, "username1", "testpass123", "user1@hotmail.com")  # TODO make a complete scenario


def cleanup(spec):
    spec.run(f"serverless remove --stage {spec['stage']} --region {spec['region']}", image='serverless_cli')
