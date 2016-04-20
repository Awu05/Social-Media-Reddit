'''

Final Project: Your Reddit Fix
Authors: Andy Wu and Steven Lyktey

'''

class Reddit:

    def get_front(self):

        '''
        This function gets the top 10 posts on Reddit's front page and
        gives us information about the user that posted these popular posts.

        We take the username of the original poster and return a list of the
        subreddits that they have posted on and we sort the list based off their
        Karma score in each subreddit.  From there, we take the subreddit with
        the most Karma score and we recommend subreddits for the user to follow.
        '''
        import praw
        user_agent = "Testing PRAW API /u/MiningReddit"
        r = praw.Reddit(user_agent=user_agent)
        #This loop gets us the top 10 posts
        for submission in r.get_front_page(limit=10):
            print submission.title
            print "Username of author: ", submission.author
            user_name = submission.author
            #Gets the username of the redditor
            user = r.get_redditor(user_name)

            #This try and catch checks if the User's profile is private
            try:
                thing_limit = 10
                gen = user.get_submitted(limit=thing_limit)
                karma_by_subreddit = {}

                #Populates the subreddit submissions list
                for thing in gen:
                    subreddit = thing.subreddit.display_name
                    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
                                                     + thing.score)
                for key, value in sorted(karma_by_subreddit.iteritems(), key=lambda (k,v): (v,k)):
                    print "%s: %s" % (key, value)
                print "\n"
                print user_name, "subreddit with most karma from submissions: r/", key, "\n"
                recom = str(r.get_subreddit_recommendations(key, omit=None))
                recomlen = len(r.get_subreddit_recommendations(key, omit=None))
                hold = ""
                for i in recom:
                    hold = hold + i

                z = 0
                print "Recommended Subreddits:\n"
                while z < recomlen * 2:
                    z += 1
                    recom2 = hold.split("'")[z]
                    print recom2
                    z += 1
                    
                
                print "------------------------------------------------------ \n"
            
            except Exception:
                print "User's Profile is private.  Cannot access data \n \n"



    def get_redditor_submissions (self, reddit_user):
        import praw
        user_agent = "Testing PRAW API /u/MiningReddit"
        r = praw.Reddit(user_agent=user_agent)

        '''
        This function prints out a list of submissions that a specific user
        has submitted to reddit, regardless of the subreddit
        '''
        user = r.get_redditor(reddit_user)
        submissions = user.get_submitted()

        self_texts = []
        for link in submissions:
            self_texts.append(link.selftext)
            print link
        print "\n\n"

    def fire_hose (self):
        #Get random subreddits and their top 10 posts
        import praw
        user_agent = "Testing PRAW API /u/MiningReddit"
        r = praw.Reddit(user_agent=user_agent)
        
        i = 0
        while(i < 10):
            subredditList = r.get_random_subreddit()
            print "Getting top 10 from subreddit:", subredditList

            testing = r.get_subreddit(str(subredditList)).get_top(limit=10)
            for x in testing:
                print x
            print "\n"
            
            i += 1

    #Imports the Subreddit Game which is saved to a different file
    def game (self):
        import Subreddit_Game


    '''
    This will handle all of the user interaction on the "Home Screen"
    '''
    def main2(self):
        while 1:
            print "------ Welcome To Your Reddit Fix ------"
            print "[1] Get the top 10 posts from the front page with additional information"
            print "[2] Get a specific Redditor's submission history"
            print "[3] FIRE HOSE (Get the top 10 Reddit posts from random subreddits)"
            print "[4] Play our Subreddit Hunt Game"
            print "[0] To Exit"
            #User Picks an option
            choice = raw_input("Please Choose an Option: ")

            if choice == '1':
                try:
                    self.get_front()
                except:
                    print "Unexpected Exception\n"

            elif choice == '2':
                try:
                    sub = raw_input("Who would you like to get the submission history of?: ")
                    self.get_redditor_submissions(sub)
                except:
                    print "Unexpected Exception\n"
                    
            elif choice == '3':
                try:
                    self.fire_hose()
                except:
                    print "Unexpected Exception\n"

            elif choice == '4':
                try:
                    self.game()
                except:
                    print "Unexpected Exception\n"
                    
            elif choice == '0':
                #If 0 is selected, exits the program
                print "Exiting Your Reddit Fix"
                exit()
            else:
                #If anything other than the numbers listed are selected, it will throw an error
                print "Please Enter A Valid Choice.\n"








#Function to make the program runable in command-line
if __name__ == "__main__":
    import sys
    x = Reddit()
    x.main2()
