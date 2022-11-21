
import pandas as pd

user = pd.read_csv("UserDetails.csv")

user["id"] = user["User"] + user["Blood Group"]

c = user["Blood Group"].value_counts()
# print(c)

user['id'] = user['id'].str.replace('+','p')
user['id'] = user['id'].str.replace('-','n')

users = user["id"].to_list()

print(users)