class User():
	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.full_name = first_name + " " + last_name

	def describe_user(self):
		return "Name: {}\nUsername: {}\nPassword: {}".format(self.full_name.title(),
			   		   										 self.username,
			   		   										 self.password)

	def greet_user(self):
		return f"Welcome back, {self.username}!"

users = []

users.append(User('robert', 'robertson', 'robtron9000', 'itsmapasswerd'))
users.append(User('jack', 'jackson', 'jdawg89', '123yupyup'))
users.append(User('john', 'johnson', 'johnsonjon20', 'sjdflejdnx'))

for user in users:
	print("\n" + user.describe_user())
	print(user.greet_user())