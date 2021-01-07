import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

REDIRECT_URL = env("REDEIRECT_URL")
CLIENT_SECRET = env("CLIENT_SECRET")
CLIENT_ID = env("CLIENT_ID")
