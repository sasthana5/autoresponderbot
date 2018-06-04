import praw
bot = praw.Reddit(user_agent='NotABot v0.1',
                  client_id='rBtV-ON0gRk_4Q',
                  client_secret='bFH60sD1LZ-N7fQEQGtdEJyemSw',
                  username='worst-bot-ever',
                  password='sXjF7ss5')
subreddit = bot.subreddit('prequelmemes')
comments = subreddit.stream.comments()
for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'hello there' in text.lower():
        # Generate a message
        message = "General Kenobi!".format(author)

        comment.reply(message) # Send message
