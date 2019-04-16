class Privileges():
    """Class for handling privileges."""

    def __init__(self, privileges):
        """Initialize attributes of Privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """List the administrator's set of privileges."""
        print("\nThis user can")
        for privilege in self.privileges:
            print('\t- ' + privilege)
