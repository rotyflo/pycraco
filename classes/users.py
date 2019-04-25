class User():
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email


    def describe_user(self):
        name = (self.first_name + ' ' + self.last_name).title()
        username = self.username
        email = self.email

        print(f"{name}, also known as {username}, can be contacted at {email}.")


    def greet_user(self):
        print(f"Hey {self.username}! Welcome back!")


# users = []
#
# users.append(User('rob', 'smith', 'robdog', 'thisguy@gmail.com'))
# users.append(User('jon', 'grape', 'grapinator', 'thatguy@pmail.com'))
# users.append(User('tom', 'miles', 'milesnmiles', 'theseguys@bmail.com'))
#
# for user in users:
#     print()
#     user.describe_user()
#     user.greet_user()
