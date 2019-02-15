from login_attempts import User
from privileges import Privileges

class Admin(User):
    """User with special privileges."""

    def __init__(self, first_name, last_name, username, password, privileges):
        """Initialize attributes of Admin."""
        super().__init__(first_name, last_name, username, password)
        self.privileges = Privileges(privileges)


johndoe = Admin('john',
                'doe',
                'johndoe',
                'password',
                ['add posts', 'delete posts', 'ban users'])

johndoe.privileges.show_privileges()
