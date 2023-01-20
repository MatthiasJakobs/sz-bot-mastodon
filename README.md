# SZbot (Mastodon)
A bot that mirrors the RSS feed of the SZ newspaper

# How to run

To run without Docker:

1. Install python requirements from `requirements.txt`
2. Create an application inside your Mastodon account. Then, copy the access token and place it into a file named `token.secret`.
3. Run `python bot.py`

To run with Docker:
1. Create image via `docker build --tag szbot .` 
2. Create container and mount this repo inside it: `docker run -d -v PATH_TO_THIS_REPO:/szbot szbot:latest`
