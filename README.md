# acme-discord-bot

This is my attempt at a simple discord bot written in python. This bot is currently hosted on heroku for free.

# Features
- Reacts to certain keywords with various GIFs and Pictures
- Allows a 1v1 mode for the board game reversi
- Mocks certain users with random capitalisation (the spongebob meme)
- Specific users are able to toggle the 'mocking feature of the bot'

# Libraries used
- discord.py by discord https://pypi.org/project/discord.py/

# content
- bot.py is the main file where all the magic / bad code is
- log.txt is a txt file that logs all the conversations in the server
- Procfile is a file that tells the heroku server which file is the worker
- board.txt is a txt file used as a temporary storage to store the state of a reversi game initialised by the bot
- requirements.txt tells the heroku server what resources are needed to run the worker file
