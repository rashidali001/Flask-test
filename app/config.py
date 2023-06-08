import os

with open("secret_key.txt", "r") as f:
    secret_key = f.read()


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or secret_key