import json

from utils import (
    get_top_users,
    get_top_retweeted_tweets,
    get_top_active_days,
    get_top_hashtags,
    open_file_json,
)


if __name__ == "__main__":
    general_json = open_file_json("farmers-protest-tweets-2021-03-5.json")
    getting = True

    while getting:
        print(
            "\n\nMenu Options: \
            \n0) Exit\
            \n1) Get top users \
            \n2) Get top retweeted tweets\
            \n3) Get top active days\
            \n4) Get top hashtags"
        )
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

        elif number == 2:
            print("\n\nTop retweeted tweets:\n")
            get_top_retweeted_tweets(general_json)

        elif number == 3:
            print("\n\nTop active days:\n")
            get_top_active_days(general_json)

        elif number == 4:
            print("\n\nTop hashtags:\n")
            get_top_hashtags(general_json)

        else:
            print("Invalid input")
            continue
