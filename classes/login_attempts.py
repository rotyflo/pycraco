class User():
    """Create a user account for a site."""

    def __init__(self, first_name, last_name, username, email):
        """Inititialize user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print out a description of current user."""
        name = (self.first_name + ' ' + self.last_name).title()
        username = self.username
        email = self.email

        print(f"{name}, also known as {username}, can be contacted at {email}.")

    def greet_user(self):
        """Welcome current user back to website."""
        print(f"Hey {self.username}! Welcome back!")

    def increment_login_attempts(self):
        """Increment login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts back to 0."""
        self.login_attempts = 0


user = User('john', 'doe', 'jdee89', 'jdee@gmail.com')

for i in range(5):
    user.increment_login_attempts()

print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
