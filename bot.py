import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment functions from the week_07 lab here

def generate_comment_0():
    names = ['Donald Trump', 'DT', 'Donald', 'POTUS', 'Ugly Orange Man']
    name = random.choice(names)

    adjs = ['dead', 'imprisoned', 'executed', 'posioned', 'assassinated']
    adj = random.choice(adjs)

    identities = ['white supremist', 'racist', 'bigot', 'KKK member', 'nazi']
    identity = random.choice(identities)

    adjs_2 = ['ugly', 'mean', 'cruel', 'stupid', 'misogynistic']
    adj_2 = random.choice(adjs_2)

    jobs = ['leader of the free world', 'president of the united states', 'leader', 'commander-in-cheif', 'president']
    job = random.choice(jobs)

    text = name + " should be " + adj + " because he is a " + identity + "! The " + adj_2 + " orange man doesn't deserve to be the " + job + "."
    return text

def generate_comment_1():
    names = ['Kamala Harris', 'KH', 'Ms. Harris', 'Future Vice President', 'Kamala']
    name = random.choice(names)

    adjs = ['elected', 'voted in', 'swarn into office', 'chosen to lead', 'supported']
    adj = random.choice(adjs)

    identities = ['strong black woman', 'successful attorney', 'strong debator', 'powerful speaker', 'committed public servant']
    identity = random.choice(identities)

    adjs_2 = ['sweet', 'funny', 'lovely', 'kind', 'serious']
    adj_2 = random.choice(adjs_2)

    jobs = ['vice president', 'first female president', 'first black female president', 'commander-in-cheif', 'VPOTUS']
    job = random.choice(jobs)

    text = name + " should be " + adj + " because she is a " + identity + "! The " + adj_2 + " Kamala deserves to be the " + job + "."
    return text

def generate_comment_2():
    names = ['Joe Biden', 'JB', 'Mr. Biden', 'Joe', 'Former Vice President JB']
    name = random.choice(names)

    adjs = ['elected', 'voted in', 'swarn into office', 'chosen to lead', 'supported']
    adj = random.choice(adjs)

    identities = ['considerate senator', 'former vice president', 'experienced debator', 'supporter of Obama', 'dedicated public servant']
    identity = random.choice(identities)

    adjs_2 = ['sweet', 'funny', 'lovely', 'kind', 'serious']
    adj_2 = random.choice(adjs_2)

    jobs = ['vice president', 'president', 'POTUS', 'commander-in-cheif', 'VPOTUS']
    job = random.choice(jobs)

    text = name + " should be " + adj + " because he is a " + identity + "! The " + adj_2 + " Kamala deserves to be the " + job + "."
    return text

def generate_comment_3():
    names = ['Mike Pence', 'MP', 'Mike', 'Pence', 'VP Mike Pence']
    name = random.choice(names)

    adjs = ['dead', 'imprisoned', 'executed', 'posioned', 'assassinated']
    adj = random.choice(adjs)

    identities = ['white supremist', 'racist', 'bigot', 'KKK member', 'nazi']
    identity = random.choice(identities)

    adjs_2 = ['ugly', 'mean', 'cruel', 'stupid', 'misogynistic']
    adj_2 = random.choice(adjs_2)

    jobs = ['leader of the free world', 'president of the united states', 'leader', 'commander-in-cheif', 'vice president']
    job = random.choice(jobs)

    text = name + " should be " + adj + " because he is a " + identity + "! The " + adj_2 + " white man doesn't deserve to be the " + job + "."
    return text

def generate_comment_4():
    names = ['Mitch McConnel', 'Senator Mitch', 'MM', 'Senator McConnel', 'Mitch']
    name = random.choice(names)

    adjs = ['dead', 'imprisoned', 'executed', 'posioned', 'assassinated']
    adj = random.choice(adjs)

    identities = ['white supremist', 'racist', 'bigot', 'KKK member', 'nazi']
    identity = random.choice(identities)

    adjs_2 = ['ugly', 'mean', 'cruel', 'stupid', 'misogynistic']
    adj_2 = random.choice(adjs_2)

    jobs = ['senator', 'senate majority leader', 'politician', 'public servant', 'leader of the senate']
    job = random.choice(jobs)

    text = name + " should be " + adj + " because he is a " + identity + "! The " + adj_2 + " white man doesn't deserve to be the " + job + "."
    return text

def generate_comment_5():
    names = ['Barack Obama', 'BO', 'Obama', 'President Obama', 'President Barack']
    name = random.choice(names)

    adjs = ['elected', 'voted in', 'swarn into office', 'chosen to lead', 'supported']
    adj = random.choice(adjs)

    identities = ['strong black man', 'passionate politician', 'successful senator', 'powerful speaker', 'committed public servant']
    identity = random.choice(identities)

    adjs_2 = ['sweet', 'funny', 'lovely', 'kind', 'serious']
    adj_2 = random.choice(adjs_2)

    jobs = ['president', 'first black president', 'first black man to hold the highest title in America', 'commander-in-cheif', 'POTUS']
    job = random.choice(jobs)

    text = name + " should be " + adj + " because he is a " + identity + "! The " + adj_2 + " Kamala deserves to be the " + job + "."
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    options = [0,1,2,3,4,5]
    choice = random.choice(options)
    if choice == 0:
        return generate_comment_0()
    elif choice == 1:
        return generate_comment_1()
    elif choice == 2:
        return generate_comment_2()
    elif choice == 3:
        return generate_comment_3()
    elif choice == 4:
        return generate_comment_4()
    elif choice == 5:
        return generate_comment_5()

# connect to reddit 
reddit = praw.Reddit('prop-rob-bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jiwfn3/from_hoangs_bot_1_biden_pledges_ambitious_climate/'
submission = reddit.submission(url=reddit_debate_url)
subreddit = reddit.subreddit('csci040temp')

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:', datetime.datetime.now())
    print('submission.title=', submission.title)
    print('submission.url=', submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    all_comments = []

    submission.comments.replace_more(limit=None)

    for comment in submission.comments.list():
        all_comments.append(comment)

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not

    not_my_comments = []
    
    for comment in all_comments:
        if comment.author != 'Responsible-Ad6086':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented == True:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        try:
            submission.reply(generate_comment())
            print('commented')
        except praw.exceptions.RedditAPIException:
            print('I am sleeping')
            time.sleep(10)
            
    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over has_not_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []

        for comment in not_my_comments:
            replied = False
            for reply in comment.replies:
                if str(reply.author) == 'Responsible-Ad6086':
                    replied = True
                elif str (reply.author) != 'Responsible-Ad6086':
                    replied = False
            if replied == False:
                comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
        comment = reddit.comment(id = random.choice(comments_without_replies))

        try:
            comment.reply(generate_comment())
            print('commented')
        except praw.exceptions.RedditAPIException:
            print('I am sleeping')
            time.sleep(10)

    """
    # EXTRA CREDIT (+2): Have your bot post new submissions to the /r/csci040 subreddit. 
    #                    These submissions should be from the top submissions of a political subreddit that supports your 
    #                    favorite presidential candidate (e.g. /r/politics or /r/conservative). 
    #                    Your bot must post at least 20 of these submissions to receive the extra credit.
    source = 'JoeBiden'
    destination = 'csci040temp'

    for submission in reddit.subreddit(source).stream.submissions():
        if not submission.is_self:
            reddit.subreddit(destination).submit(submission.title, url=submission.url)
    """

    # EXTRA CREDIT (+1): HAVE YOUR BOT UPVOTE ANY SUBMISSIONS MENTIONING YOUR FAVORITE CANDIDATE.
    favorite_canidates = ['joe', 'biden', 'kamala', 'harris', 'joe biden', 'kamala harris']

    sub_title = submission.title.lower()
    for candidate in favorite_canidates:
        if candidate in sub_title:
            submission.upvote()
    """
    # this code searches the entire subreddit however I kept running into rate limit errors.
    for submission in subreddit.hot(limit=1):
        sub_title = submission.title.lower()
        for candidate in favorite_canidates:
            if candidate in sub_title:
                submission.upvote()
    for submission in subreddit.top(limit=1):
        sub_title = submission.title.lower()
        for candidate in favorite_canidates:
            if candidate in sub_title:
                submission.upvote()
    for submission in subreddit.new(limit=1):
        sub_title = submission.title.lower()
        for candidate in favorite_canidates:
            if candidate in sub_title:
                submission.upvote()
    """

    # EXTRA CREDIT (+1): HAVE YOUR BOT UPVOTE ANY COMMENTS MENTIONING YOUR FAVORITE CANDIDATE.
    favorite_canidates = ['joe', 'biden', 'kamala', 'harris', 'joe biden', 'kamala harris']

    for comment in submission.comments.list():
        for candidate in favorite_canidates:
            if candidate in comment.body:
                comment.upvote()

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    if random.random() < 0.5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        top_threads = list(reddit.subreddit('csci040temp').top(time_filter='all'))
        top_threads.append(submission)
        random_submission = random.choice(top_threads)
        print('random_submission = ', random_submission)
        submission = reddit.submission(id = random_submission)
        print('you are commenting in a new submission')