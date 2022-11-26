import pandas as pd
from instaloader import Instaloader, Profile
# 1. Loading in the data
# Reading the data from the csv
data = pd.read_csv('test.csv')
# Getting the profile urls
urls = data['Profile URL']

def getFollowerCount(PROFILE):
    # using the instaloader module to get follower counts from this programmer
    # https://stackoverflow.com/questions/52225334/webscraping-instagram-follower-count-beautifulsoup
    try:
        L = Instaloader()
        profile = Profile.from_username(L.context, PROFILE)
        print(PROFILE, 'has', profile.followers, 'followers')
        return(profile.followers)
    except Exception as exception :
        print(exception, False)
        return(0)

# Follower count List
followerCounts = []
# This loop will fetch the follower count for each user
for url in urls:
    # Getting the profile username from the URL by removing the instagram.com
    # portion and the backslash at the end of the url
    url_dirty = url.replace('https://www.instagram.com/', '')
    url_clean = url_dirty[:-1]
    followerCounts.append(getFollowerCount(url_clean))

# Converting the list to a series, adding it to the dataframe, and writing it to
# a csv
data['Follower Count'] = pd.Series(followerCounts)
data.to_csv('IG_Audience.csv')