import instaloader

# Get instance
insta = instaloader.Instaloader()

# Change this code
USERNAME=''
PASSWORD=''


insta.login(user=USERNAME, passwd=PASSWORD)
print(insta.context)