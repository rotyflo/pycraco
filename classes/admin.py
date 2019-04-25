from users import User
from privileges import Privileges

class Admin(User):
    """Create a user with special powers."""

    def __init__(self, first_name, last_name, username, email):
        """Inherit properties from User class."""
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges(["can add post",
                                      "can delete post",
                                      "can ban user"])


employee = Admin('tommy', 'jones', 'thedude', 'tomjon@email.com')

employee.privileges.show_privileges()
