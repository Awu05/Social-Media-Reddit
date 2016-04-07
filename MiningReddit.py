import praw
import webbrowser


r = praw.Reddit(user_agent="test")

#subredditList = r.get_popular_subreddits(limit=20)
i = 0
while(i < 100):
    subredditList = r.get_random_subreddit()
    print subredditList
    i += 1

'''
for subreddit in subredditList:
    print subreddit
'''

'''
r = praw.Reddit('CIS 400: Social Media Mining Experiment')
r.set_oauth_app_info(client_id='7jP2S9cmElab6g',
                     client_secret='NA0QS5UlRNHDQsbgVXhYrwYIWTQ',
                     redirect_uri='http://127.0.0.1:65010/authorize_callback')


url = r.get_authorize_url('uniqueKey', 'identity', True)
webbrowser.open(url)


access_information = r.get_access_information('g21Px-zMUk1J0wX6UwddkVjpWS4')
'''


#https://www.reddit.com/api/v1/authorize/?state=uniqueKey&redirect_uri=http%3A%2F%2F127.0.0.1%3A65010%2Fauthorize_callback&response_type=code&client_id=7jP2S9cmElab6g&duration=permanent&scope=identity

#http://127.0.0.1:65010/authorize_callback?state=uniqueKey&code=g21Px-zMUk1J0wX6UwddkVjpWS4
