import tweepy
import os
import json
import webbrowser
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk


############# tkinter
root = Tk()
root.title("今日 Japanese Twitter Translator")
root.iconbitmap(r'C:\Users\emelu\pypro\emicon.ico')
root.configure(background='black')
#root.geometry("800x500")
#############


consumer_key = 'rAmyMnPFEaKqU2drbowJpK3mX'
consumer_secret = os.environ.get('TWITTER_SECRET_KEY')
access_token = '1341136443960401922-nIRuho8dntG3DzoKl2t0nURTkzBXkr'
access_token_secret = os.environ.get('TWITTER_TOKEN_SECRET')
auth_v1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_v1.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_v1)

############### trend data
def get_trends():
    trends_raw = api.trends_place(id=23424856)#jap23424856 ny2459115
    #trends_neat = json.dumps(trends_raw, indent=4, sort_keys=True)
    trend = trends_raw[0]['trends'][0]['name']
    return trend
###############


################ search trend, get tweet
def get_tweet(trend, rank):
    #trend_search_raw = api.search(q=trend, result_type='popular')
#    if len(trend_search_raw) == 0:
    trend_search_raw = api.search(q=trend)
    trend_search_status = trend_search_raw[0]
    trend_search_str = json.dumps([trend_search_status._json for status in trend_search_raw], indent=4, sort_keys=True)
    trend_search_json = json.loads(trend_search_str)
    trend_tweet = trend_search_json[rank]
    return trend_tweet
################


################ Tweet info class
class tweetinfo:
    def __init__(self, tweet_json):
        """
        i=0
        if len(tweet_json['text']) > 39:
            fixed_tweet = ''
            for char in tweet_json['text']:
                if char == '\n':
                    i -= 1
                    char = ' - '
                fixed_tweet = fixed_tweet + char
                i += 1
                if i%40 == 0 and i != 0:
                    fixed_tweet = fixed_tweet + '\n'
        else:
            fixed_tweet = tweet_json['text']
        """
        pp_data = Image.open(urlopen(tweet_json['user']['profile_image_url']))

        self.text = tweet_json['text'] #fixed_tweet
        self.user = tweet_json['user']['screen_name']
        self.pp = pp_data
        self.id = tweet_json['id_str']
################


################ go to browser
def goToBrowser():
    #to add an arguement
#from functools import partial
#(...)
#action_with_arg = partial(action, arg)
#button = Tk.Button(master=frame, text='press', command=action_with_arg)
    link = 'twitter.com/anyuser/status/' + tweet_1_info.id
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(link, autoraise=True)
###############


############### Create tweet PhotoImage
def tweetPage():
    homeScreenTitleLabel.grid_forget()
    homeScreenWelcomeLabel.grid_forget()
    tweetPageButton.grid_forget()

    intro.grid(row=0, column=0)
    userFrame.grid(row=1, column=0)
    ppLabel.pack(side='left')
    usernameLabel.pack(side='right')
    #ppLabel.grid(row=0, column=1)
    #usernameLabel.grid(row=0, column=2)
    tweet1Label.grid(row=2, column=0)
    linkButton.grid(row=3, column=0)
###############

trend_1 = get_trends()
tweet_1 = get_tweet(trend_1, 0)
tweet_1_info = tweetinfo(tweet_1)
username = '@' + tweet_1_info.user


userFrame = Frame(root, bg='black')
intro = Label(root, text="TOP TWEET IN JAPAN TODAY:", font=(None, 20), padx=50, pady=50, fg='white', bg='black')
#profile picture
pp = ImageTk.PhotoImage(tweet_1_info.pp)
ppLabel = Label(userFrame, image=pp)
#profile picture
#usernameLabel
usernameLabelText = StringVar()
usernameLabelText.set(username)
usernameLabel = Entry(userFrame, font=(None, 20), state="readonly", textvariable=usernameLabelText, width=20, bd=0, fg='white')
usernameLabel.configure(readonlybackground="black", justify='left')
#username label
tweet1Label = Label(root, text=tweet_1_info.text, font=('Meiryo', 15), padx=30, pady=20, borderwidth=2, relief="solid", fg='white', bg='black', highlightbackground='white', anchor='w', justify='left')
linkButton = Button(root, text="Take Me There!", font=(None, 25), command=goToBrowser, fg='white', bg='black') #command=translate
homeScreenTitleLabel = Label(root, text="今日　Japanese Twitter Translator", font=(None, 35), padx=50, pady=50, fg='white', bg='black')
homeScreenWelcomeLabel = Label(root, text="Click Below to Get Started.", font=(None, 25), padx=50, pady=50, fg='white', bg='black')
tweetPageButton = Button(root, text="ツ", font=('Meiryo', 20), command=tweetPage, fg='white', bg='black', padx=50, pady=-10)

homeScreenTitleLabel.grid(row=0, column=0)
homeScreenWelcomeLabel.grid(row=1, column=0)
tweetPageButton.grid(row=2, column=0)
# intro.grid(row=0, column=0)
# userFrame.grid(row=1, column=0)
# ppLabel.pack(side='left')
# usernameLabel.pack(side='right')
# #ppLabel.grid(row=0, column=1)
# #usernameLabel.grid(row=0, column=2)
# tweet1Label.grid(row=2, column=0)
# linkButton.grid(row=3, column=0)

root.mainloop()

#only allow it to retrieve data once a day
"""
dkdkdkdkd 16
"""
