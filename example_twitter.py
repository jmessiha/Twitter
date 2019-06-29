from twitter import Tweeter

t = Tweeter('netflix',mode='top',k=2,emojis=True)
# mode = 'top'	# section: top, latest, news, broadcasts
				# mode = 'profile' to search profile (example, realDonaldTrump)
				# k = number of pages of tweets, approx. tweets 20 per page.
				# emojis = False removes emojis
				# emojis = True converts emojis to readable text (i.e. sad-face)
				
tweets = t.get_tweets()

print(tweets[0])

#takes tweet or comment as input
comments = t.get_comments(tweets[0])	# gets comments for that tweet

print(comments[0])