#This program receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. The program prints the user's name and the group they belong to.

def groups_per_user(data):
    result = {}
    for group, users in data.items():
        for user in users:
            if user in result:
                result[user].append(group)
            else:
                result[user] = [group]
    return result

data = {
    "admins": ["john", "alice"],
    "developers": ["jane", "john"],
    "designers": ["alice", "peter"]
}

result = groups_per_user(data)
print(result)
