import praw
import webbrowser

'''
r = praw.Reddit(user_agent="test")

#subredditList = r.get_popular_subreddits(limit=20)
i = 0
while(i < 100):
    subredditList = r.get_random_subreddit()
    print subredditList
    i += 1
'''

'''
for subreddit in subredditList:
    print subreddit
'''


#Get information about a specific user, it currently shows the karma in which
#they got from

user_agent = "Testing PRAW API /u/MiningReddit"
r = praw.Reddit(user_agent=user_agent)


#Get top stories from front page of reddit
#Idk why I found this
for submission in r.get_front_page(limit=10):
    print submission.title
    print "Username of author: ", submission.author
    user_name = submission.author
    user = r.get_redditor(user_name)

    thing_limit = 10
    gen = user.get_submitted(limit=thing_limit)
    karma_by_subreddit = {}
    for thing in gen:
        subreddit = thing.subreddit.display_name
        karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
                                         + thing.score)
    import pprint
    pprint.pprint(karma_by_subreddit)
    print "\n"



'''
#Gets the amount of karma from the specific subreddit they got it from
user_name = "painmatrix" #Random User
user = r.get_redditor(user_name)

thing_limit = 10
gen = user.get_submitted(limit=thing_limit)
karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
                                     + thing.score)
import pprint
pprint.pprint(karma_by_subreddit)
'''

'''
user = r.get_redditor('kayjay25')
submissions = user.get_submitted()

self_texts = []
for link in submissions:
    self_texts.append(link.selftext)
    print link
'''



