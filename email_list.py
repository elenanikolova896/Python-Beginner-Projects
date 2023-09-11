#This program  receives a dictionary, which contains domain names as keys, and a list of users as values. Then it generates a list that contains complete email adresses 

def email_list(data):
    emails = []
    for domain, users in data.items():
        for user in users:
            email = "{}@{}".format(user, domain)
            emails.append(email)
    return emails

data = {
    "gmail.com": ["diana.prince", "clark.kent", "bruce.wayne"],
    "yahoo.com": ["peter.parker", "tony.stark"]
}

result = email_list(data)
for email in result:
    print(email)
