friends = []

def friendorfoe(names):
    for name in names:
        if len(name) == 4:
            friends.append(name)

friendorfoe(["Ryan", "Kieran", "Jason", "Yous"])
print(friends)
