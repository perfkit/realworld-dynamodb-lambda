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

class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.token = None

    def description(self):
        return f"user {self.username} with email {self.email} and password {self.password}"

    def create(self, spec):
        logging.info(f"[Creating] {self.description()}.")
        self.token = createUser(spec, self.username, self.password, self.email).json()['user']['token']

    def login(self, spec):
        logging.info(f"[Login] {self.description()}.")
        self.token = loginUser(spec, self.email, self.password).json()['user']['token']

    def get(self, spec):
        logging.info(f"[Get] {self.description()}.")
        # TODO

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
        'user': config  # config can contain: { 'password': password, 'email': email, 'image': image, 'bio': bio }
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
    resp = requests.post(url=getEndpointURL(spec, f"profiles/{username}/follow"), json=data,
                         headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def unfollowUser(spec, token, username):
    resp = requests.delete(url=getEndpointURL(spec, f"profiles/{username}/follow"),
                           headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


# Articles API

def createArticle(spec, token, title, description, body):
    data = {
        'article': {
            'title': title,
            'description': description,
            'body': body
        }
    }
    resp = requests.post(url=getEndpointURL(spec, "articles"), json=data, headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def getArticle(spec, token, slug):
    resp = requests.get(url=getEndpointURL(spec, f"articles/{slug}"), headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def updateArticle(spec, token, slug, config):  # token must correspond to article.author!
    data = {
        'article': config  # contains at least one: {'title': title, 'description': desc, 'body': body}
    }
    resp = requests.put(url=getEndpointURL(spec, f"articles/{slug}"), json=data,
                        headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def deleteArticle(spec, token, slug):
    resp = requests.delete(url=getEndpointURL(spec, f"articles/{slug}"), headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def favoriteArticle(spec, token, slug):
    data = {}
    resp = requests.post(url=getEndpointURL(spec, f"articles/{slug}/favorite"), json=data,
                         headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def unfavoriteArticle(spec, token, slug):
    resp = requests.delete(url=getEndpointURL(spec, f"articles/{slug}/favorite"),
                           headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def listArticles(spec, token, params):  # params contains at most one of these: {'tag', 'author', 'favorited'}
    resp = requests.get(url=getEndpointURL(spec, "articles"), headers={'Authorization': 'Token ' + token},
                        params=params)
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def getArticlesFeed(spec, token, params):  # params can contain: {'limit': 20, 'offset': 0}
    resp = requests.get(url=getEndpointURL(spec, "articles/feed"), headers={'Authorization': 'Token ' + token},
                        params=params)
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def getTags(spec):
    resp = requests.get(url=getEndpointURL(spec, "tags"))
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


# Comments API

def createComment(spec, token, slug, body):
    data = {
        'comment': {
            'body': body
        }
    }
    resp = requests.post(url=getEndpointURL(spec, f"articles/{slug}/comments"), json=data,
                         headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def getComments(spec, token, slug):
    resp = requests.get(url=getEndpointURL(spec, f"articles/{slug}/comments"),
                        headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def deleteComment(spec, token, slug, comment_id):  # token must correspond to comment.author!
    resp = requests.delete(url=getEndpointURL(spec, f"articles/{slug}/comments/{comment_id}"),
                           headers={'Authorization': 'Token ' + token})
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


# Utils API

def ping(spec):
    resp = requests.get(url=getEndpointURL(spec, "ping"))
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


def purgeData(spec):
    resp = requests.delete(url=getEndpointURL(spec, "__TESTUTILS__/purge"))
    if resp.status_code == 200:
        return resp
    else:
        raise Exception(f"Error code {resp.status_code}: {resp.content}")


# SB entry points

# before first start: run 'npm install' !
def prepare(spec):
    log = spec.run(f"serverless deploy --stage {spec['stage']} --region {spec['region']}", image='serverless_cli')
    spec['endpoint'] = re.findall(r"https://([-\w.]+)/", log)[-1]
    logging.info(f"service endpoint={spec['endpoint']}")


def invoke(spec):
    #logging.info(f"{createUser(spec, 'username1', 'testpass123', 'user1@hotmail.com').content}")  # TODO make a complete scenario
    logging.info(f"{loginUser(spec,  'user1@hotmail.com', 'testpass123').content}")


def cleanup(spec):
    spec.run(f"serverless remove --stage {spec['stage']} --region {spec['region']}", image='serverless_cli')
