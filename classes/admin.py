from users import User

class Admin(User):
    """Create a user with special powers."""

    def __init__(self, first_name, last_name, username, email):
        """Inherit properties from User class."""
        super().__init__(first_name, last_name, username, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(self.first_name.title() + " " + privilege + "s.")


employee = Admin('tommy', 'jones', 'thedude', 'tomjon@email.com')

employee.show_privileges()
