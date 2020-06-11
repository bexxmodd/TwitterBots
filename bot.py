import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("yXwfT8Iz8VnnbjPRRZMCqOjvj",
            "9SVanNYZGGKV7mafJLDhg1NeAbyMths0l7VqmZ4PvnTKpQrMXr")

auth.set_access_token("3532655353-31eK8ZGCmCBOpl0ge3boj5d9JW6ZgpVxkpfLnPx",
    "RX0ojGYw8ZazmJn36KA82E7ygsLr4HUtowjNHlQZGHAHW")

# Create API object
twitter = tweepy.API(auth)

# Verify Creds
try:
    twitter.verify_credentials()
    print("Authentication Passed!")
except AttributeError:
    print("Can't Authenticate...")

# twitter.update_status("Bot says: Hello world!")