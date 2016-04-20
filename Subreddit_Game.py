import praw
import webbrowser

class subredditGame:

    def game():
        
        #Get information about a specific user, it currently shows the karma in which
        #they got from

        user_agent = "Testing PRAW API /u/MiningReddit"
        r = praw.Reddit(user_agent=user_agent)

        #Reddit Wiki Game

        start = str(r.get_random_subreddit())
        end = str(r.get_random_subreddit())
        current = start
        path = []
        numtimes = 0
        print "----- Welcome to the Subreddit Hunt -----\n"
        print "The objective is to get from the \nstarting subreddit to the ending subreddit.\n"

        #If start is equal to end, repick end
        while start == end:
            end = r.get_random_subreddit()

        #Checks to see if the current and end subreddits match
        while current != end:
            print "Your CURRENT Subreddit is:", current
            print "Your ENDING Subreddit is:", end, "\n"
            print 'Hint: You can type "Repick" to change your \ncurrent subreddit if you are stuck or if \nno available subreddits are shown.\n'
            
            recom = str(r.get_subreddit_recommendations(current, omit=None))
            recomlen = len(r.get_subreddit_recommendations(current, omit=None))
            recomlen2 = len(r.get_subreddit_recommendations(end, omit=None))

            #If the recommended subreddit list has less than 1, repick starting position
            if(recomlen < 2):
                print "Repicking current subreddit due to lack of choices.\n"
                current = str(r.get_random_subreddit())
                recom = str(r.get_subreddit_recommendations(current, omit=None))
                recomlen = len(r.get_subreddit_recommendations(current, omit=None))
                while start == end:
                    current = str(r.get_random_subreddit())
                    
                #current = start
                print "Your NEW CURRENT Subreddit is:", current, "\n"

            if(recomlen2 < 2):
                print "Repicking ENDING subreddit due to lack of choices.\n"
                end = str(r.get_random_subreddit())
                while start == end:
                    end = str(r.get_random_subreddit())

                current = start
                print "Your NEW ENDING Subreddit is:", current, "\n"

            print "Your Choices of Subreddits To Pick Are:\n"
                
            hold = ""
            for i in recom:
                hold = hold + i

            z = 0

            while z < recomlen * 2:
                z += 1
                recom2 = hold.split("'")[z]
                print recom2
                z += 1

            choice = raw_input("Please Choose a Subreddit: ")
            if(choice.lower() == "repick"):
                print "Repicking CURRENT subreddit.\n"
                current = str(r.get_random_subreddit())
                choice = current
            current = choice
            path.append(choice)
            numtimes += 1
            if current.lower() == end.lower():
                break

            print "----------------------------------------------------------\n\n"


        print "\nCongradulations on getting to the Subreddit!"
        print "You used", numtimes, "move(s) to get to", end
        print "\nThe path you used to get to", end, "is", path


    game()
    

