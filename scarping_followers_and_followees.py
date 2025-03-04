# Importing Libraries
import instaloader
import pandas as pd 

# Username and password
USERNAME=''
PASSWORD=''

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
bot.login(user=USERNAME, passwd=PASSWORD)

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, USERNAME)

# Retrieving the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]
# Converting the data to a DataFrame
followers_df = pd.DataFrame(followers)
# Storing the results in a CSV file
followers_df.to_csv('followers.csv', index=False)

# Retrieving the usernames of all followings
followings = [followee.username for followee in profile.get_followees()]
# Converting the data to a DataFrame
followings_df = pd.DataFrame(followings)
# Storing the results in a CSV file
followings_df.to_csv('followings.csv', index=False)

print("comparing lists")
for person_i_follow in followings:
  if (person_i_follow not in followers):
    print(person_i_follow)