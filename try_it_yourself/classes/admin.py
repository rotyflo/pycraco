from login_attempts import User

class Admin(User):
    """User with special privileges."""

    def __init__(self, first_name, last_name, username, password, privileges):
        """Initialize attributes of Admin."""
        super().__init__(first_name, last_name, username, password)
        self.privileges = privileges

    def show_privileges(self):
        """List the administrator's set of privileges."""
        print("\nList of privileges:")
        for privilege in self.privileges:
            print('\t' + privilege)


johndoe = Admin('john',
                'doe',
                'johndoe',
                'password',
                ['can add post', 'can delete post', 'can ban user'])

johndoe.show_privileges()
