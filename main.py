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


if __name__ == "__main__":
    general_json = open_file_json("farmers-protest-tweets-2021-03-5.json")

    getting = True

    while getting:
        print("\n\nIngrese alguna nueva opcion: \n0) Exit\n1) Get top users ")
        number = input()
        try:   
            number = int(number)
        except: 
            print("Invalid input")
            continue
        if number == 1:
            print("\n\nTop users:\n")
            get_top_users(general_json)
        elif number == 0:
            getting = False 

