import json

def open_file_json(file_name):
    with open("farmers-protest-tweets-2021-03-5.json", 'r') as jsonFile:
        lines = jsonFile.readlines()

    general_json = [ json.loads(line) for line in lines]
    return general_json

def get_top_users(jsonFile):

    users = {}
    for tweet in jsonFile:
        if tweet['user']['username'] not in users:
            users[tweet['user']['username']] = 1
        else:
            users[tweet['user']['username']] += 1

    #obtain the top 10 users
    top_users = sorted(users.items(), key=lambda x: x[1], reverse=True)[:10]

    for i in range(10):
        print(f"  {i+1}) {top_users[i][0]}: {top_users[i][1]} ")

def get_top_retweeted_tweets(jsonFile):
    retweeted_tweets = {}
    for tweet in jsonFile:
        retweeted_tweets[tweet['id']] = [tweet['retweetCount'],tweet['user']['username'],tweet["content"]]

    #obtain the top 10 retweeted tweets
    top_retweeted_tweets = sorted(retweeted_tweets.items(), key=lambda x: x[1][0], reverse=True)[:10]

    for i in range(10):
        print(f"{i+1}) [{top_retweeted_tweets[i][1][0]}] {top_retweeted_tweets[i][1][1]}: {top_retweeted_tweets[i][1][2]} ")

if __name__ == "__main__":
    general_json = open_file_json("farmers-protest-tweets-2021-03-5.json")

    getting = True

    while getting:
        print("\n\nMenu Options: \
            \n0) Exit\
            \n1) Get top users \
            \n2) Get top retweeted tweets")
        number = input("Enter your choice: ")
        try:   
            number = int(number)
        except: 
            print("Invalid input")
            continue

        if number == 0:
            getting = False 

        elif number == 1:
            print("\n\nTop users:\n")
            get_top_users(general_json)
        elif number ==2 :
            print("\n\nTop retweeted tweets:\n")
            get_top_retweeted_tweets(general_json)
