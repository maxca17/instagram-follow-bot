import instaloader
import time
import pandas as pd
L = instaloader.Instaloader()
username = 'chicken171717'
password = 'Applejack17!'
# Login or load session
L.login(username, password)        # (login)

qqq = input('Is list already populated: (y or n)')


if qqq == 'n':
    account = input('Please enter account username: ')
# Print list of followees
    follow_list = []
    count = 0
    for followee in profile.get_followers():
        follow_list.append(followee.username)
        file = open("test.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        print(follow_list[count])
        count = count + 1
else:
    pass
# (likewise with profile.get_followers())

#data = pd.read_csv('test.txt')
#Obtain profile metadata
data = open('test.txt', 'r')
yes = data.read()
for person in yes:
    profile = instaloader.Profile.from_username(L.context, yes)
    followers = profile.get_followers()
    number_of_followers = followers.count
    time.sleep(15)

#print(number_of_followers)