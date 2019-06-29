# Twitter
Extract tweets and comments

twitter.py is not publicly available, you need to message me directly to get access to this file.

    from twitter import Tweeter

    t = Tweeter('netflix',mode='top',k=2,emojis=True)
    # mode = 'top'	# section: top, latest, news, broadcasts
            # mode = 'profile' to search profile (example, realDonaldTrump)
            # k = number of pages of tweets, approx. tweets 20 per page.
            # emojis = False removes emojis
            # emojis = True converts emojis to readable text (i.e. sad-face)

    tweets = t.get_tweets()

    #takes tweet or comment as input
    comments = t.get_comments(tweets[0])	# gets comments for that tweet

Example outputs

    print(tweets[0])
    {'text': u'I was too tired to watch movie tonight so I decided to watch Evangelion on Netflix . pic.twitter.com/sw0VOviaaH', 'num_likes': u'36850', 
     'user': u'HIDEO_KOJIMA_EN', 'num_comments': u'494', 'time_stamp': u'6:17 PM - 28 Jun 2019', 'num_retweets': u'5963', 'type': 0, 'id': u'1144776977464696833'}


    print(comments[0])
    {'text': u'You like Anime!!??', 'num_likes': u'36852', 'user': u'johnnydork', 'num_comments': u'494', 
     'time_stamp': u'6:17 PM - 28 Jun 2019', 'num_retweets': u'5964', 'type': u'1144776977464696833', 'id': u'1144777747195191296'}
