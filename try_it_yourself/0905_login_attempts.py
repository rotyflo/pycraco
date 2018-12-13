class User():
	"""Represent user of a site."""

	def __init__(self, first_name, last_name, username, password):
		"""Initialize attributes of user."""
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = password
		self.full_name = first_name + " " + last_name
		self.login_attempts = 0

	def describe_user(self):
		"""Print extensive amount of information about user."""
		print("\nName: {}\nUsername: {}\nPassword: {}"
			.format(self.full_name.title(),
					self.username,
			   		self.password))

	def greet_user(self):
		"""Print a greeting that welcomes user back."""
		print(f"Welcome back, {self.username}!")

	def increment_login_attempts(self):
		"""Increase login attempts by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset login attempts to 0."""
		self.login_attempts = 0

users = []

users.append(User('robert', 'robertson', 'robtron9000', 'itsmapasswerd'))

users[0].increment_login_attempts()
users[0].increment_login_attempts()
users[0].increment_login_attempts()

print(users[0].login_attempts)

users[0].reset_login_attempts()

print(users[0].login_attempts)