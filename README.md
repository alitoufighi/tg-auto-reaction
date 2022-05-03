What's This?
---
We had a tough discussion in the general students' group of our school, and after a while I decided to give up talking and instead, started sending poo reactions to their messages. What a relief, right?

This is the automated-poo-react-machine so that you won't miss any of their BSs!

Usage
---
MTProto is the Telegram's API for client applications. It requires you to obtain an `API_ID` and an `API_HASH` by visiting [my.telegram.org/apps](https://my.telegram.org/apps) and entering your own credentials. This script uses Pyrogram, a powerful MTProto implementation.

Though this is a pretty simple script, it has its own headaches in setting up. If you run this script for the first time, you'll see that you'll need to log into your Telegram account, similar to any new other Telegram clients. Pyrogram caches the session and some other data in a SQLite database, stored in a file named `auto-reaction.session`. **My suggestion if you want to use Docker is to log in once into your account to create this database file, then build a docker image containing this file and then run as a docker container. Otherwise, run normally. Also note that you cannot have simulatenous sessions running together.**

The script expects these variables to be set in the environment:
* `API_ID`: Your Telegram API ID received via my.telegram.org
* `API_HASH`: Your Telegram API hash received via my.telegram.org
* `VICTIM_USER_IDS`: Comma separated user IDs of the victims who will receive reactions.
* `VICTIM_GROUP_IDS`: Comma separated group IDs where the victims will receive reactions.

You can either pass these variables directly to the program or store them in a `.env` file (containing `NAME=VALUE` lines). 

To sum up, you'll need to log into your account once without docker:
```bash
python3 -m venv venv && source venv/bin/activate  # Or any other way you create your virtualenvs
pip install -r requirements.txt
API_ID=12345 \
  API_HASH=abcdef \
  VICTIM_USER_IDS=12345 \
  VICTIM_GROUP_IDS=12345 \
    python main.py
```
Then, you'll be prompted to enter your phone number, the login code sent to your account, and, if set, your 2FA password.

After entering these data correctly, a `auto-reaction.session` file will be created. Then, build a docker image containing this file:
```bash
docker build -t auto-reaction .  # Existing Dockerfile copies everything in the context root directory inside the container
```
Finally, run your container:
```bash
docker run --restart unless-stopped auto-reaction
```

Finding the user and group IDs
----
To find them, you can use `util.py`. This file uses the same session as the main script, with the only difference that instead of reacting to a specific message with an emoji, it prints all the incoming messages it gets with their metadata. You can:
* Send a message to your Saved Messages and see the printed output to find your own user ID; or
* Send a message to the target group and find the group ID inside the `chat` field; or
* Send a message to the victim user to find their user ID.

Have fun!
