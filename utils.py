import json


def open_file_json(file_name):
    with open(file_name, "r") as jsonFile:
        lines = jsonFile.readlines()

    general_json = [json.loads(line) for line in lines]
    return general_json


def get_top_users(jsonFile):

    users = {}
    for tweet in jsonFile:
        if tweet["user"]["username"] not in users:
            users[tweet["user"]["username"]] = 1
        else:
            users[tweet["user"]["username"]] += 1

    # obtain the top 10 users
    top_users = sorted(users.items(), key=lambda x: x[1], reverse=True)[:10]

    for i in range(10):
        print(
            f"0{i+1}) {top_users[i][0]}: {top_users[i][1]} "
            if i < 9
            else f"{i+1}) {top_users[i][0]}: {top_users[i][1]} "
        )


def get_top_retweeted_tweets(jsonFile):
    retweeted_tweets = {}
    for tweet in jsonFile:
        retweeted_tweets[tweet["id"]] = [
            tweet["retweetCount"],
            tweet["user"]["username"],
            tweet["content"],
        ]

    # obtain the top 10 retweeted tweets
    top_retweeted_tweets = sorted(
        retweeted_tweets.items(), key=lambda x: x[1][0], reverse=True
    )[:10]

    for i in range(10):
        print(
            f"0{i+1}) [{top_retweeted_tweets[i][1][0]}] {top_retweeted_tweets[i][1][1]}: {top_retweeted_tweets[i][1][2]} "
            if i < 9
            else f"{i+1}) [{top_retweeted_tweets[i][1][0]}] {top_retweeted_tweets[i][1][1]}: {top_retweeted_tweets[i][1][2]} "
        )


def get_top_active_days(jsonFile):
    active_days = {}
    for tweet in jsonFile:
        date = tweet["date"][:10]
        if date not in active_days:
            active_days[date] = 1
        else:
            active_days[date] += 1

    # obtain the top 10 active days
    top_active_days = sorted(active_days.items(), key=lambda x: x[1], reverse=True)[:10]

    for i in range(10):
        print(
            f"0{i+1}) {top_active_days[i][0]}: {top_active_days[i][1]} "
            if i < 9
            else f"{i+1}) {top_active_days[i][0]}: {top_active_days[i][1]} "
        )


def get_top_hashtags(jsonFile):
    hashtags = {}
    for tweet in jsonFile:
        list = [tag for tag in tweet["content"].split() if tag.startswith("#")]
        for hashtag in list:
            if hashtag not in hashtags:
                hashtags[hashtag] = 1
            else:
                hashtags[hashtag] += 1

    # obtain the top 10 hashtags
    top_hashtags = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)[:10]

    for i in range(10):
        print(
            f"0{i+1}) {top_hashtags[i][0]}: {top_hashtags[i][1]} "
            if i < 9
            else f"{i+1}) {top_hashtags[i][0]}: {top_hashtags[i][1]} "
        )
